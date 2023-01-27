import os
import json
import base64
from google.cloud import pubsub_v1
import functions_framework


@functions_framework.cloud_event
def restaurant_orders_pubsub(cloud_event):
  project_id = 'kubernetics-366409'
  # Read the Pub/Sub message
  message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8')
  message = json.loads(message)

  # Get the order type from the message
  order_type = message['type']

  # Initialize the Pub/Sub client
  publisher = pubsub_v1.PublisherClient()

  # Publish the message to the appropriate Pub/Sub topic
  if order_type == "takeout":
    topic_name = "restaurant_takeout_orders"
  elif order_type == "eat-in":
    topic_name = "restaurant_eat-in_orders"
  else:
    # Ignore all other messages
    return

  # Publish the message
  topic_path = publisher.topic_path(project_id, topic_name)
  publisher.publish(topic_path, data=json.dumps(message).encode('utf-8'))

