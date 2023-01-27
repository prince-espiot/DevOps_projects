import json
import sys

import pika

from xprint import xprint


class ShoppingEventProducer:

    def __init__(self):
        # Do not edit the init method.
        # Set the variables appropriately in the methods below.
        self.connection = None
        self.channel = None

    def initialize_rabbitmq(self):
        # To implement - Initialize the RabbitMq connection, channel, exchange and queue here
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='shopping_events_exchange',exchange_type='x-consistent-hash',durable=True)
        #self.channel.queue_declare(queue='entry_type',exclusive=True)
        
        
        xprint("ShoppingEventProducer initialize_rabbitmq() called")

    def publish(self, shopping_event):
        xprint("ShoppingEventProducer: Publishing shopping event {}".format(vars(shopping_event)))
        # To implement - publish a message to the Rabbitmq here
        routing_key = shopping_event.product_number
        xprint("Printing routhing key {}".format(routing_key))
        message =  json.dumps(vars(shopping_event))
        self.channel.basic_publish(exchange='shopping_events_exchange', routing_key=routing_key, body=message,properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                                ))
        # Use json.dumps(vars(shopping_event)) to convert the shopping_event object to JSON
        
    def close(self):
        # Do not edit this method
        self.channel.close()
        self.connection.close()
