from google.cloud import pubsub_v1
import os

# Set up the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp.json"

# Initialize a Pub/Sub client
publisher = pubsub_v1.PublisherClient()
# Replace 'my-project-id' and 'my-topic' with your project and topic details
topic_path = publisher.topic_path('my-project-id', 'my-topic')

# The data to publish
data = "Hello, World!"
# Data must be a bytestring
data = data.encode("utf-8")

# Publish data
future = publisher.publish(topic_path, data)
print(f"Published message ID: {future.result()}")
