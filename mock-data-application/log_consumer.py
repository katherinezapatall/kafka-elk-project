from confluent_kafka import Consumer, KafkaError

# Define Kafka broker address
kafka_broker = 'localhost:29092'

# Create Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': kafka_broker,
    'group.id': 'log_consumer_group',  # Choose a unique consumer group ID
    'auto.offset.reset': 'earliest'  # Start consuming from the beginning of the topic
}

# Create Kafka consumer instance
consumer = Consumer(consumer_config)

# Subscribe to the Kafka topic
consumer.subscribe(['orders'])

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages every 1 second

        if msg is None:
            continue
        if msg.error():
            # Handle any Kafka errors
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of topic")
            else:
                print(f"Error: {msg.error().str()}")
        else:
            # Print the received log message
            print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass
finally:
    # Close the Kafka consumer
    consumer.close()
