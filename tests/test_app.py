import unittest
import requests

class TestTemperatureApp(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'  # URL вашого Flask додатку

    def test_home_page(self):
        # Надсилаємо GET запит на головну сторінку
        response = requests.get(f'{self.BASE_URL}/')
        
        # Перевіряємо, чи отримали код відповіді 200 (ОК)
        self.assertEqual(response.status_code, 200)

    def test_metrics(self):
        # Надсилаємо GET запит на /metrics (метрики для Prometheus)
        response = requests.get(f'{self.BASE_URL}/metrics')
        
        # Перевіряємо, чи отримали код відповіді 200
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
