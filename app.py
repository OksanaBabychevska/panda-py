import os
from flask import Flask, render_template, request
from prometheus_client import start_http_server, Summary, generate_latest
import time

app = Flask(__name__)

flask_port = os.getenv('FLASK_PORT', 5000)
metrics_port = os.getenv('METRICS_PORT', 8000)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
@app.route('/', methods=['GET', 'POST'])
def index():
    fahrenheit = None  
    celsius = None

    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])
            fahrenheit = celsius * 9 / 5 + 32
        except ValueError:
            fahrenheit = "Invalid input. Please enter a number."

    return render_template('index.html', celsius=celsius, fahrenheit=fahrenheit)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == '__main__':
    start_http_server(int(metrics_port)) 
    app.run(host='0.0.0.0', port=int(flask_port))
