import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()