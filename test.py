from flask import json
from flask import request
from flask import jsonify
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

@app.route('/')
def api_root():
    return('Hello, World!!!')

@app.route('/gitlab', methods=['POST'])
def api_gitlab_message():
    if request.headers['Content-Type'] == 'application/json':
        message = json.dumps(request.json)
        print(message)
        return(message)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=False)