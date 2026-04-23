#!/usr/bin/env python3
from typing import Any, List, Optional, Union
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
    def validate(self, data: List[int]) -> bool:
        return len(data) > 0

    def process(self, data: List[int]) -> str:
        if not self.validate(data):
            raise ValueError("Invalid input")
        count = len(data)
        total = sum(data)
        return (
            f"Processed {count} numeric values, sum={total}, "
            f"avg={total/count:.1f}"
        )


class TextProcessor(DataProcessor):
    def validate(self, data: str) -> bool:
        return len(data) > 0

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid input")
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split())} words"
        )


class LogProcessor(DataProcessor):
    """Warning: index() will raise ValueError when substring is not found"""
    def validate(self, data: str) -> bool:
        """Returns:
            bool: True if "ERROR: " or "INFO: " is in data and is not at the
            end of the str, else False
        """
        if "ERROR: " not in data and "INFO: " not in data:
            return False
        hit = "ERROR: " if "ERROR: " in data else "INFO: "
        if data.index(hit) != 0 and len(data) == len(hit):
            return False
        return True

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid input")
        is_error = "ERROR: " in data
        if is_error:
            substr = "ERROR: "
            status = "[ALERT] ERROR"
        else:
            substr = "INFO: "
            status = "[INFO] INFO"
        msg_i = data.index(substr) + len(substr)
        msg = data[msg_i:]
        return f"{status} level detected: {msg}"


def print_factory(
    inp: Optional[dict[str, Union[List[int], str]]] = None
) -> None:
    had_inp = inp is not None
    if not inp:
        inp = {
            'nbrlst': [1, 2, 3, 4, 5],
            'text': "Hello Nexus World",
            'status_report': "ERROR: Connection timeout",
        }
    if len(inp) != 3:
        print("Not enough inputs")
        return

    try:
        processors_data = [
            (NumericProcessor(), inp['nbrlst'], "Numeric", "data"),
            (TextProcessor(), inp['text'], "Text", "data"),
            (LogProcessor(), inp['status_report'], "Log", "entry"),
        ]

        if not had_inp:
            print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

            for processor, data, ptype, entry in processors_data:
                print(f"\nInitializing {ptype} Processor...")
                print(f"Processing data: {data}")
                is_verified = (
                    f"{ptype} {entry}" if processor.validate(data) else "Not"
                )
                print(f"Validation: {is_verified} verified")
                result = processor.process(data)
                print(processor.format_output(result))

        else:
            print("\n=== Polymorphic Processing Demo ===\n")
            print("Processing multiple data types through same interface...")
            i = 0
            for processor, data, _, _ in processors_data:
                print(f"Result {i + 1}: {processor.process(data)}")
                i += 1

    except (KeyError, ValueError) as e:
        print(f"Operation aborted: {e}")


if __name__ == "__main__":
    print_factory()
    print_factory({
        'nbrlst': [3, 2, 1],
        'text': "Monday mornings",
        'status_report': "INFO: System ready",
    })
    print("\nFoundation system online. Nexus ready for advanced streams.")
