#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            for num in data:
                int(num)
            if len(data):
                return True
            return False
        except TypeError:
            return False
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise TypeError("Invalid input")
        except TypeError as e:
            return f"Operation aborted: {e}"
        count = len(data)
        total = sum(data)
        return (
            f"Processed {count} numeric values, sum={total}, "
            f"avg={total/count:.1f}"
        )


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if len(data):
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid input")
        except (TypeError, ValueError) as e:
            return f"Operation aborted: {e}"
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split())} words"
        )


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if ("ERROR" in data or "INFO" in data) and ": " in data:
            if data[0] != ":" and data[-2] != ":":
                return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid input")
        except (TypeError, ValueError) as e:
            return f"Operation aborted: {e}"
        first_half = data.split(": ")[0]
        second_half = data.split(": ")[1]
        return (
            f"[{"ALERT" if "ERROR" in data else "INFO"}] "
            f"{first_half} level detected: {second_half}"
        )


def print_factory() -> None:
    processors_data = [
        (NumericProcessor(), [1, 2, 3, 4, 5]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), "ERROR: Connection timeout"),
    ]
    process_type = [
        ("Numeric", "data"),
        ("Text", "data"),
        ("Log", "entry"),
    ]

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    for i, (processor, data) in enumerate(processors_data):
        print(f"\nInitializing {process_type[i][0]} Processor...")
        print(f'Processing data: {repr(data)}')
        if processor.validate(data):
            print(
                f"Validation: {process_type[i][0]} {process_type[i][1]} "
                "verified"
            )
        else:
            print("Validation: Not verified!")
        result = processor.process(data)
        print(processor.format_output(result))

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    inputs = [
        [3, 2, 1],
        "Happy monday",
        "INFO: System ready",
    ]

    for i, (processor, _) in enumerate(processors_data):
        print(f"Result {i+1}: {processor.process(inputs[i])}")
    print("\nFoundation system online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    print_factory()
