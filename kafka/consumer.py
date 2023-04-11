import json
import sys
from confluent_kafka import Consumer, KafkaError, KafkaException
from database.db import SessionLocal
from repository.pumps import PumpsDAL
from dto.pumps import pumps


conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': "foo",
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)
db = SessionLocal()
running = True


def basic_consume_loop():
    try:
        consumer.subscribe(["pumps1"])

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                data = msg.value().decode('utf-8')

                try:
                    data = json.loads(data)
                    val = pumps.Pumps(id=data['id'], pressure=data['pressure'],
                                      temperature=data['temperature'], speed=data['speed']
                                      )
                    pump = PumpsDAL(db).get_data(idx=data['id'])
                    if not pump:
                        PumpsDAL(db).insert_data(data=val)

                    print(val)

                except ValueError:
                    pass
    finally:
        consumer.close()


def shutdown():
    running = False


basic_consume_loop()



