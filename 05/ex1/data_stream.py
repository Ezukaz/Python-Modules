#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union, Tuple


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
        self.data: List[str] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def _filter_by_type(self, data_batch: List[Any]) -> List[str]:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        self.data = self._filter_by_type(data_batch)
        if criteria == "high priority":
            self.filter_priority()
        return self.data

    @staticmethod
    def _is_high_priority(k: Optional[str], v: str) -> bool:
        return False

    def filter_priority(self) -> None:
        priority = []
        for x in self.data:
            k, v = x.split(":") if ":" in x else (None, x)
            if self._is_high_priority(k, v):
                priority.append(x)
        self.data = priority

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}

    @staticmethod
    def _is_valid(data: str, criteria: str) -> bool:
        if not isinstance(data, str):
            return False
        if not data.startswith(criteria):
            return False
        if data.count(":") != 1:
            return False
        try:
            key, value = data.split(":")
            if not key.strip() or not value.strip():
                return False
            float(value)
            return True
        except (ValueError, IndexError):
            return False


class SensorStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id, "Sensor", "Environmental Data")

    @staticmethod
    def _is_high_priority(k: Optional[str], v: str) -> bool:
        try:
            val = float(v)
            return any((
                k == "temp" and float(val) > 40.0,
                k == "humidity" and int(val) > 65,
                k == "pressure" and int(val) > 1023,
            ))
        except ValueError:
            return False

    def _filter_by_type(self, data_batch: List[Any]) -> List[str]:
        allowed = ("temp:", "humidity:", "pressure:")
        return [
            x for x in data_batch if any(self._is_valid(x, c) for c in allowed)
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        temps = []
        for x in self.data:
            if x.startswith("temp:"):
                try:
                    temps.append(float(x.split(":")[1]))
                except ValueError:
                    continue
        return {
            "count": len(self.data),
            "avg_temp": round(sum(temps) / len(temps), 1) if temps else 0.0
        }

    def process_batch(self, data_batch: List[Any]) -> str:
        self.data = data_batch
        stats = self.get_stats()
        return (
            f"{stats['count']} reading(s) processed, "
            f"avg temp: {stats['avg_temp']}°C"
        )


class TransactionStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id, "Transaction", "Financial Data")

    @staticmethod
    def _is_high_priority(k: Optional[str], v: str) -> bool:
        return int(v) > 1000

    def _filter_by_type(self, data_batch: List[Any]) -> List[str]:
        allowed = ("sell:", "buy:")
        return [
            x for x in data_batch if any(self._is_valid(x, c) for c in allowed)
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        net = 0
        for x in self.data:
            if ":" not in x:
                continue
            k, v = x.split(":")
            if k == "buy":
                net += int(v)
            elif k == "sell":
                net -= int(v)
        return {
            "count": len(self.data),
            "net_flow": net
        }

    def process_batch(self, data_batch: List[Any]) -> str:
        self.data = data_batch
        stats = self.get_stats()
        return (
            f"{stats['count']} operation(s), "
            f"net flow: {stats['net_flow']:+d} unit(s)"
        )


class EventStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id, "Event", "System Events")

    @staticmethod
    def _is_high_priority(k: Optional[str], v: str) -> bool:
        return v.lower() == "error"

    def _filter_by_type(self, data_batch: List[Any]) -> List[str]:
        return [
            x for x in data_batch if x in ("login", "error", "logout")
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        err_count = sum(1 for x in self.data if x == "error")
        return {
            "count": len(self.data),
            "error": err_count
        }

    def process_batch(self, data_batch: List[Any]) -> str:
        self.data = data_batch
        stats = self.get_stats()
        return f"{stats['count']} event(s), {stats['error']} error(s) detected"


class StreamProcessor():
    def __init__(self) -> None:
        self._streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self._streams.append(stream)

    def process_all(self, data_batch: List[str]) -> None:
        for stream in self._streams:
            try:
                filtered = stream.filter_data(data_batch)
                print(f"\nInitializing {stream.type} Stream...")
                print(f"Stream ID: {stream.id}, Type: {stream.batch_type}")
                print(f"Processing {stream.type} batch: {filtered}")
                analysis = stream.process_batch(filtered)
                print(f"{stream.type} analysis: {analysis}")
            except Exception as e:
                print(f"\nError in {stream.type} Stream: {e}")
                print("Skipping to next available stream...")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001"),
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
        "buy:75",
        "error"
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
            "humidity:60",
            "sell:1500",
            "logout",
            "humidity:70"
        ],
        # [
        #     "temp:22.5",
        #     "login",
        #     "error",
        #     "pressure:1024",
        #     "error",
        #     "error",
        #     "buy:250",
        #     "humidity:65",
        #     "sell:1500",
        #     "logout",
        #     "buy:750"
        # ],
        # [
        #     "temp:22.5:",
        #     "error",
        #     "error",
        #     "pressure:1013",
        #     "temp:45.5",
        #     "temp: 37.0",
        #     "sell:230",
        #     "sell:6000",
        #     "buy:100",
        #     "humidity:65",
        #     "sell:150",
        #     "error",
        #     "buy:75"
        # ],
    ]
    new_streams: List[Tuple[DataStream, str]] = [
        (SensorStream("SENSOR_001"), "reading"),
        (TransactionStream("TRANS_001"), "operation"),
        (EventStream("EVENT_001"), "event")
    ]
    for i, batch in enumerate(more_batches):
        print(f"\nBatch {i+1} Results:")
        for stream, process in new_streams:
            stream.filter_data(batch)
            print(
                f"- {stream.type} data: {len(stream.data)} "
                f"{process}(s) processed"
            )

        results = [
            f"{len(new_streams[0][0].filter_data(batch, 'high priority'))} "
            "critical sensor alert(s)",
            f"{len(new_streams[1][0].filter_data(batch, 'high priority'))} "
            "large transaction(s)",
            f"{len(new_streams[2][0].filter_data(batch, 'high priority'))} "
            "important event(s)",
        ]
        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {results}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
