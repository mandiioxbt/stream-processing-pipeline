# Stream Processing Pipeline

Event-driven stream processing with exactly-once semantics and dead letter queue.

## Features
- Kafka consumer with exactly-once guarantees
- Windowed aggregations (tumbling, sliding, session)
- Dead letter queue for poison messages
- Schema registry integration (Avro, Protobuf)

## Pipeline
```
Kafka → Deserialize → Process → Aggregate → Sink (DB/Topic)
                          ↓ (on error)
                    Dead Letter Queue
```

## License: MIT
