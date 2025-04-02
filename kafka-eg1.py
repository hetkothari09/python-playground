from ensurepip import bootstrap

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "my_topic",
    bootstrap_servers=["localhost:9092"],
    enable_auto_commit=False,
    auto_offset_reset="earliest",
    group_id="my_group_id",
    value_deserializer=lambda x: x.decode('utf-8')
)

for message in consumer:
    print("Message: ", message.value)