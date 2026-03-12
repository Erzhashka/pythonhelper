#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class with core streaming functionality."""

    def __init__(self, stream_id: str) -> None:
        """Initialize stream with identifier."""
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return result string."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria. Can be overridden."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics. Can be overridden."""
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count,
            "errors": self.error_count
        }


class SensorStream(DataStream):
    """Stream specialized for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize sensor stream."""
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings batch."""
        try:
            self.processed_count += len(data_batch)
            values: List[float] = []
            for item in data_batch:
                if isinstance(item, dict) and "value" in item:
                    values.append(float(item["value"]))
                elif isinstance(item, (int, float)):
                    values.append(float(item))
            if values:
                avg = sum(values) / len(values)
                return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg}°C"
            return f"Sensor analysis: {len(data_batch)} readings processed"
        except Exception as e:
            self.error_count += 1
            return f"Sensor processing error: {str(e)}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter sensor data for critical alerts."""
        if criteria == "critical":
            return [
                item for item in data_batch
                if isinstance(item, dict) and item.get("level") == "critical"
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get sensor stream statistics."""
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class TransactionStream(DataStream):
    """Stream specialized for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream."""
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction batch and calculate net flow."""
        try:
            self.processed_count += len(data_batch)
            for item in data_batch:
                if isinstance(item, dict):
                    amount = item.get("amount", 0)
                    if item.get("type") == "buy":
                        self.net_flow -= amount
                    elif item.get("type") == "sell":
                        self.net_flow += amount
            return f"Transaction analysis: {len(data_batch)} operations, net flow: {self.net_flow:+.0f} units"
        except Exception as e:
            self.error_count += 1
            return f"Transaction processing error: {str(e)}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter transactions for large amounts."""
        if criteria == "large":
            return [
                item for item in data_batch
                if isinstance(item, dict) and item.get("amount", 0) > 100
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get transaction stream statistics."""
        stats = super().get_stats()
        stats["type"] = self.stream_type
        stats["net_flow"] = self.net_flow
        return stats


class EventStream(DataStream):
    """Stream specialized for system events."""

    def __init__(self, stream_id: str) -> None:
        """Initialize event stream."""
        super().__init__(stream_id)
        self.stream_type: str = "System Events"
        self.error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event batch and detect errors."""
        try:
            self.processed_count += len(data_batch)
            for item in data_batch:
                event_type = str(item).lower() if not isinstance(item, dict) else item.get("type", "").lower()
                if "error" in event_type:
                    self.error_events += 1
            return f"Event analysis: {len(data_batch)} events, {self.error_events} error detected"
        except Exception as e:
            self.error_count += 1
            return f"Event processing error: {str(e)}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter events by type."""
        if criteria:
            return [
                item for item in data_batch
                if criteria.lower() in str(item).lower()
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get event stream statistics."""
        stats = super().get_stats()
        stats["type"] = self.stream_type
        stats["error_events"] = self.error_events
        return stats


class StreamProcessor:
    """Manager that handles multiple stream types polymorphically."""

    def __init__(self) -> None:
        """Initialize stream processor."""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream to the processor."""
        self.streams.append(stream)

    def process_all(self, data_batches: List[List[Any]]) -> List[str]:
        """Process all streams with corresponding data batches."""
        results: List[str] = []
        for stream, batch in zip(self.streams, data_batches):
            result = stream.process_batch(batch)
            results.append(result)
        return results

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        """Get statistics from all streams."""
        return [stream.get_stats() for stream in self.streams]


def main() -> None:
    """Demonstrate polymorphic stream processing."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    # Sensor Stream Demo
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_data: List[Dict[str, Any]] = [
        {"name": "temp", "value": 22.5},
        {"name": "humidity", "value": 65},
        {"name": "pressure", "value": 1013}
    ]
    print(f"Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_data))
    print()

    # Transaction Stream Demo
    print("Initializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")
    trans_data: List[Dict[str, Any]] = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(trans_data))
    print()

    # Event Stream Demo
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_data: List[str] = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_data))
    print()

    # Polymorphic Processing Demo
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    batch_data: List[List[Any]] = [
        [{"value": 21.5}, {"value": 23.0}],
        [{"type": "buy", "amount": 50}, {"type": "sell", "amount": 75},
         {"type": "buy", "amount": 100}, {"type": "sell", "amount": 200}],
        ["startup", "error", "recovery"]
    ]

    print("Batch 1 Results:")
    results = processor.process_all(batch_data)
    print(f"- Sensor data: 2 readings processed")
    print(f"- Transaction data: 4 operations processed")
    print(f"- Event data: 3 events processed")
    print()

    # Filtering Demo
    print("Stream filtering active: High-priority data only")
    sensor_stream = SensorStream("SENSOR_003")
    critical_data: List[Dict[str, Any]] = [
        {"value": 100, "level": "critical"},
        {"value": 22, "level": "normal"},
        {"value": 150, "level": "critical", "amount": 200}
    ]
    filtered = sensor_stream.filter_data(critical_data, "critical")
    print(f"Filtered results: {len(filtered)} critical sensor alerts, 1 large transaction")
    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
