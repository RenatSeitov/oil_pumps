from confluent_kafka import Producer
import json
import random


conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'oil_pumps'
}

producer = Producer(conf)


def send_data_to_kafka(topic, data):
    producer.produce(topic, key=None, value=data)
    producer.flush()


count = 0
while count < 10:
    data = {"id": random.randint(1, 100),
            "pressure": random.randint(50, 100),
            "temperature": random.randint(20, 40),
            "speed": random.randint(1000, 2000)}
    json_data = json.dumps(data)
    send_data_to_kafka("pumps1", json_data)
    print("msg sendS")
    count += 1
