#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string. Can be overridden by subclasses."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric data."""

    def process(self, data: Any) -> str:
        """Process numeric data and return statistics."""
        if not self.validate(data):
            return "Invalid numeric data"
        try:
            total = sum(data)
            avg = total / len(data)
            return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            return f"Processing error: {str(e)}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a list of numbers."""
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def format_output(self, result: str) -> str:
        """Format numeric output."""
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Processor specialized for text data."""

    def process(self, data: Any) -> str:
        """Process text data and return analysis."""
        if not self.validate(data):
            return "Invalid text data"
        try:
            char_count = len(data)
            word_count = len(data.split())
            return f"Processed text: {char_count} characters, {word_count} words"
        except Exception as e:
            return f"Processing error: {str(e)}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a string."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Format text output."""
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """Processor specialized for log entries."""

    def process(self, data: Any) -> str:
        """Process log entry and extract level and message."""
        if not self.validate(data):
            return "Invalid log entry"
        try:
            if ":" in data:
                level, message = data.split(":", 1)
                level = level.strip()
                message = message.strip()
            else:
                level = "INFO"
                message = data
            return f"[ALERT] {level} level detected: {message}"
        except Exception as e:
            return f"Processing error: {str(e)}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a valid log string."""
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        """Format log output."""
        return f"Output: {result}"


def main() -> None:
    """Demonstrate polymorphic data processing."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    # Numeric Processor Demo
    print("Initializing Numeric Processor...")
    numeric_proc = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print(f"Validation: {'Numeric data verified' if numeric_proc.validate(numeric_data) else 'Failed'}")
    print(numeric_proc.format_output(numeric_proc.process(numeric_data)))
    print()

    # Text Processor Demo
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print(f"Validation: {'Text data verified' if text_proc.validate(text_data) else 'Failed'}")
    print(text_proc.format_output(text_proc.process(text_data)))
    print()

    # Log Processor Demo
    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print(f"Validation: {'Log entry verified' if log_proc.validate(log_data) else 'Failed'}")
    print(log_proc.format_output(log_proc.process(log_data)))
    print()

    # Polymorphic Processing Demo
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    test_data: List[Union[List[int], str]] = [
        [1, 2, 3],
        "Nexus Online",
        "INFO: System ready"
    ]

    for i, (proc, data) in enumerate(zip(processors, test_data), 1):
        result = proc.process(data)
        print(f"Result {i}: {result}")

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
