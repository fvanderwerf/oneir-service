
from flask import Flask, request

service = Flask("oneir-service")

@service.route("/api/v1/oneir/command", methods=["POST"])
def oneir_command():
    if request.data == "off":
        return "ok"
    else:
        return "nok"

if __name__ == "__main__":
    service.run(host='0.0.0.0', port=8080)

