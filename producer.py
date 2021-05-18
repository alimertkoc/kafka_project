from flask import request, jsonify, Flask, make_response
from kafka import KafkaProducer
from time import sleep

app = Flask(__name__)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'], api_version=(0,10,1))

@app.route('/', methods=['POST'])
def sendMessage():
    message = request.get_json()
    return make_response(message, 201)
    	
app.run()