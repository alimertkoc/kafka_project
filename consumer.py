from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('project', bootstrap_servers=['kafka:9092'], api_version=(0, 10))

for message in consumer:
    print(message.value)