from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    enable_auto_commit=False,
    auto_offset_reset='earliest'
)

consumer.subscribe(topics=['my_topic'])

'''
poll method is used to fetch the messages from the subscribed topics
Also it allows us to specify a time that the consumer should wait before returning the messages
it returns an empty dict if no messages are present
'''

while True:
    msg = consumer.poll(timeout_ms=1000)
    if msg:
        # for topic, partition, offset, key, value in msg.items():
        #     print("Topic: {}, Parition: {}, Offset: {}, Key: {}, Value: {}", topic, partition, offset, key, value.decode('utf-8'))
        for tp, records in msg.items():  # tp stands for Topic and Partition and record stands for Consumer record
            for record in records:
                print("Topic: {}, Parition: {}, Offset: {}, Key: {}, Value: {}", tp.topic, tp.partition, record.offset, record.key,
                      record.value.decode('utf-8'))
    else:
        print("There are no new messages!")