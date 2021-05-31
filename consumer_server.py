from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest"
)

consumer.subscribe(['servicecalls'])

for message in consumer:
    print(message.value)