#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(
        self,
        stream_id: str,
        stream_type: str,
        batch_type: str,
    ) -> None:
        self.id = stream_id
        self.type = stream_type
        self.batch_type = batch_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        ...

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}

    @staticmethod
    def is_valid(data: str, criteria: Any) -> bool:
        if not isinstance(data, str):
            return False
        if not data.startswith(criteria):
            return False
        try:
            split = data.split(":")
            if len(split) != 2:
                return False
            float(split[1])
            return True
        except Exception:
            return False


class SensorStream(DataStream):
    def __init__(self, id: str, type: str, batch_type: str) -> None:
        super().__init__(id, type, batch_type)

    def filter_data(self, data_batch: List[str], criteria: Optional[str] = None) -> List[str]:
        self.data = [
            x for x in data_batch
            if self.is_valid(x, ("temp:", "humidity:", "pressure:"))
        ]

        if criteria == "high-priority":
            high_priority = []
            for x in self.data:
                k, v = x.split(":")
                if (
                    (k == "temp" and float(v) > 40.0) or
                    (k == "humidity" and int(v) > 65) or
                    (k == "pressure" and int(v) > 1023)
                ):
                    high_priority.append(x)
            return high_priority
        return self.data

    def get_stats(self) -> Dict[str, Union[int, float]]:
        temps = [
            x.split(":")[1] for x in self.data if self.is_valid(x, "temp:")
        ]
        return {
            "count": len(self.data),
            "avg_temp": round(sum(map(float, temps))/len(temps), 1)
            if temps else 0.0
        }

    def process_batch(self, data_batch: List[str]):
        self.filter_data(data_batch)
        stats = self.get_stats()
        return (
            f"{stats['count']} reading(s) processed, "
            f"avg temp: {stats['avg_temp']}°C"
        )


class TransactionStream(DataStream):
    def __init__(self, id: str, type: str, batch_type: str) -> None:
        super().__init__(id, type, batch_type)

    def filter_data(
        self,
        data_batch: List[str],
        criteria: str | None = None
    ) -> List[str]:
        self.data = [
            x for x in data_batch if self.is_valid(x, ("sell:", "buy:"))
        ]

        if criteria == "high-priority":
            high_priority = []
            for x in self.data:
                _, v = x.split(":")
                if int(v) > 1000:
                    high_priority.append(x)
            return high_priority
        return self.data

    def get_stats(self) -> Dict[str, int]:
        net = 0
        for x in self.data:
            k, v = x.split(":")
            if k == "buy":
                net += int(v)
            elif k == "sell":
                net -= int(v)
        return {
            "count": len(self.data),
            "net_flow": net
        }

    def process_batch(self, data_batch: List[str]) -> str:
        self.filter_data(data_batch)
        stats = self.get_stats()
        return (
            f"{stats['count']} operation(s), net flow: "
            f"{'+' if int(stats['net_flow']) >= 0 else '-'}"
            f"{stats['net_flow']} unit(s)"
        )


class EventStream(DataStream):
    def __init__(self, id: str, type: str, batch_type: str) -> None:
        super().__init__(id, type, batch_type)

    def filter_data(self, data_batch: List[str]) -> List[str]:
        self.data = [
            x for x in data_batch if x in ("login", "error", "logout")
        ]
        return self.data

    def get_stats(self) -> Dict[str, int]:
        err_count = 0
        for x in self.data:
            if x == "error":
                err_count += 1
        return {
            "count": len(self.data),
            "error": err_count
        }

    def process_batch(self, data_batch: List[str]) -> str:
        self.filter_data(data_batch)
        stats = self.get_stats()
        return f"{stats['count']} event(s), {stats['error']} error(s) detected"


class StreamProcessor():
    def __init__(self) -> None:
        self._streams = []

    def add_stream(self, stream: DataStream) -> None:
        self._streams.append(stream)

    def process_all(self, data_batch: List[str]) -> None:
        for stream in self._streams:
            print(f"\nInitializing {stream.type} Stream...")
            print(f"Stream ID: {stream.id}, Type: {stream.batch_type}")
            print(
                f"Processing {stream.type} "
                f"Batch: {stream.filter_data(data_batch)}"
            )
            print(
                f"{stream.type} analysis: {stream.process_batch(data_batch)}"
            )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    streams = [
        SensorStream("SENSOR_001", "Sensor", "Environmental Data"),
        TransactionStream("TRANS_001", "Transaction", "Financial Data"),
        EventStream("EVENT_001", "Event", "System Events"),
    ]
    batch = [
        "temp:22.5",
        "login",
        "error",
        "pressure:1013",
        "buy:100",
        "humidity:65",
        "sell:150",
        "logout",
        "buy:75"
    ]
    manager = StreamProcessor()
    for stream in streams:
        manager.add_stream(stream)
    manager.process_all(batch)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    more_batches = [
        [
            "temp:50",
            "login",
            "error",
            "pressure:1050",
            "buy:1000",
            "humidity:65",
            "sell:1500",
            "logout",
            "buy:750"
        ],
        [
            "temp:22.5",
            "login",
            "error",
            "pressure:1024",
            "error",
            "error",
            "buy:250",
            "humidity:65",
            "sell:1500",
            "logout",
            "buy:750"
        ],
        [
            "temp:22.5:",
            "error",
            "error",
            "pressure:1013",
            "temp:45.5",
            "temp: 37.0",
            "sell:230",
            "sell:6000",
            "buy:100",
            "humidity:65",
            "sell:150",
            "error",
            "buy:75"
        ],
    ]
    streams = [
        SensorStream("SENSOR_001", "Sensor", "reading"),
        TransactionStream("TRANS_001", "Transaction", "operation"),
        EventStream("EVENT_001", "Event", "event")
    ]
    for i, batch in enumerate(more_batches):
        print(f"\nBatch {i+1} Results:")
        for stream in streams:
            stream.filter_data(batch)
            print(
                f"- {stream.type} data: {len(stream.data)} "
                f"{stream.batch_type}(s) processed"
            )

        print("\nStream filtering active: High-priority data only")
        print(
            "Filtered results: "
            f"{len(streams[0].filter_data(batch, "high-priority"))} "
            "critical sensor alert(s), "
            f"{len(streams[1].filter_data(batch, "high-priority"))} "
            "large transaction(s)"
        )

    print("All streams processed successfully. Nexus throughput optimal.")
