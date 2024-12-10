from kafka import KafkaProducer
import json

# Callback function to handle delivery reports
def on_send_success(record_metadata):
    print(f"Message delivered to {record_metadata.topic} [{record_metadata.partition}]")

def on_send_error(excp):
    print(f"Message delivery failed: {excp}")

# Initialize the producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define the message (event)
message = {'event': 'user_signup', 'user_id': 123}

# Send the message to the Kafka topic 'user_events'
producer.send('user_events', value=message).add_callback(on_send_success).add_errback(on_send_error)

# Wait for any outstanding messages to be delivered and delivery reports to be received
producer.flush()

print("Message sent!")
