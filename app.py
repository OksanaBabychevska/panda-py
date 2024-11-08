import os
from flask import Flask, render_template, request
from prometheus_client import start_http_server, Summary, generate_latest
import time

app = Flask(__name__)

# Задаємо порти для Flask і для метрик
flask_port = os.getenv('FLASK_PORT', 5000)  # Порт для Flask додатку
metrics_port = os.getenv('METRICS_PORT', 8000)  # Порт для метрик

# Створення метрики для обробки часу запитів
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Обробка основного запиту
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

# Маршрут для метрик Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest(), 200

# Запуск серверу для метрик і Flask додатку
if __name__ == '__main__':
    # Запуск HTTP серверу для метрик Prometheus на порту metrics_port
    start_http_server(int(metrics_port))  
    # Запуск Flask додатку на порту flask_port
    app.run(host='0.0.0.0', port=int(flask_port))
