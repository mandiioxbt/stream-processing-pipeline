# Stream Processing Pipeline

Event-driven stream processing with exactly-once semantics.

## Features
- Kafka consumer with exactly-once guarantees
- Windowed aggregations
- Dead letter queue
- Schema registry integration

## Topology
```
Kafka → Deserialize → Process → Aggregate → Sink (DB/Topic)
            ↓
       Dead Letter Queue
```

## License
MIT
