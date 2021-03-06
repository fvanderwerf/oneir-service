
from flask import Flask, request
from flask.ext.cors import CORS
import pika
import json


# Create our connection object, passing in the on_open method

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
        '172.17.0.7',
        5672,
        '/',
        credentials)

pikaconn = pika.BlockingConnection(parameters=parameters)
channel = pikaconn.channel()
channel.queue_declare(queue='oneir')

service = Flask("oneir-service")
CORS(service)

@service.route("/api/v1/oneir/config", methods=["GET"])
def get_config():
    return flask.jsonify(**{})


@service.route("/api/v1/oneir/command", methods=["POST"])
def oneir_command():
    data = request.get_json()
    if "command" in data:
        channel.basic_publish(exchange='', routing_key='oneir', body=json.dumps(data["command"]))
    
    return ('', 204)

if __name__ == "__main__":
    service.run(host='0.0.0.0', port=8080)

