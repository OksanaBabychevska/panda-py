import os
from flask import Flask, render_template, request
from prometheus_client import Summary, generate_latest, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

# Ініціалізація Flask додатку
app = Flask(__name__)

# Порти, на яких буде працювати додаток
flask_port = os.getenv('FLASK_PORT', 5000)
metrics_port = os.getenv('METRICS_PORT', 8000)

# Оголошуємо метрику для вимірювання часу обробки запитів
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Маршрут для головної сторінки
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

# Маршрут для метрик, який використовує Prometheus для збору даних
@app.route('/metrics')
def metrics():
    return generate_latest(), 200

# Запуск Flask додатку з прометеусом на одному порті
if __name__ == '__main__':
    # Інтеграція Prometheus метрик як middleware
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()  # Всі запити до /metrics будуть оброблятися окремо
    })
    
    # Запуск Flask серверу
    app.run(host='0.0.0.0', port=int(flask_port))
