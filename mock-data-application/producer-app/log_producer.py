from confluent_kafka import Producer
import logging
import time
import json
import random

# Define Kafka broker address
kafka_broker = 'kafka2:9092'

# Create Kafka producer configuration
producer_config = {
    'bootstrap.servers': kafka_broker
}

# Create Kafka producer instance
producer = Producer(producer_config)

# Configure logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# List of possible log sources (components)
log_sources = ['authentication', 'http_request_processing']

# List of possible HTTP status codes
http_status_codes = [200, 400, 401, 402, 403, 404, 500]

# Simulate random log messages
for i in range(1, 1000000):
    log_source = random.choice(log_sources)

    if log_source == 'authentication':
        log_message = {
            'timestamp': time.time(),
            'source': log_source,
            'message': f'User authentication id #{i} failed',
            'remote_ip': '10.10.10.10'
        }
    elif log_source == 'http_request_processing':
        status_code = random.choice(http_status_codes)
        log_message = {
            'timestamp': time.time(),
            'source': log_source,
            'message': f'HTTP request processing log message #{i}',
            'http_status_code': status_code,
            'remote_ip': '10.x.10.x'
        }

    # Produce the log message to the Kafka topic
    producer.produce('logging', key=str(i), value=json.dumps(log_message))
    producer.flush()

    logger.info(f'Sent {log_source} log message #{i}')
    time.sleep(random.uniform(0.1, 1.0))
