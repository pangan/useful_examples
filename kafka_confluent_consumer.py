from confluent_kafka import Consumer, KafkaError, OFFSET_BEGINNING

def amir_commit(b, c):

    print ('Commit!!! {}'.format(b))

def read_kafka():

    c = Consumer({
        'bootstrap.servers': 'amir-dev.dev.op5.com',
        'group.id': 'mygroup3',
        'client.id': 'client-1',
        'enable.auto.commit': True,
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'}
    })

    def my_assign(consumer, partitions):
        for p in partitions:
            p.offset = OFFSET_BEGINNING
        print('assign', partitions)
        consumer.assign(partitions)

    c.subscribe(['amir-topic-1'], on_assign=my_assign)

    try:
        while True:


            msg = c.poll(0)

            if msg is None:
               # yield None
                continue

            if msg.error():
                print (msg.error())
                if msg.error().code() == KafkaError._PARTITION_EOF:

                    #yield None
                    continue
                else:
                    #yield str(msg.error())
                    print(msg.error())
                    break
            print ('Received message: {}'.format(msg.value().decode('utf-8')))
            #yield 'Received message: {}'.format(msg.value().decode('utf-8'))
            #yield '->{}'.format(msg)
    except KeyboardInterrupt:
        pass

    finally:
        print("closing ...")
        c.close()


kf=read_kafka()
# while True:
#
#     a = next(kf)
#     if a:
#         print(a)
