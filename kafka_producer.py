from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['kafka-broker:9092']
)

producer.send("my_topic", value="Helow from producer from python!".encode('utf-8'))