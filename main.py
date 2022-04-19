import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get/', methods=['GET'])
def respond():
    response = {"RANDOM": random.randrange(10)}

    # Return the response in json format
    return jsonify(response)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
