import unittest
import requests

class TestTemperatureApp(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'  # URL of the Flask app

    def test_convert_temperature(self):
        # Send POST request with valid celsius value
        response = requests.post(f'{self.BASE_URL}/convert', data={'celsius': 25})
        self.assertEqual(response.status_code, 200)  # Expect status 200
        self.assertIn('fahrenheit', response.json())  # Ensure 'fahrenheit' is in the response JSON

    def test_invalid_temperature(self):
        # Send POST request with invalid celsius value
        response = requests.post(f'{self.BASE_URL}/convert', data={'celsius': 'invalid'})
        self.assertEqual(response.status_code, 400)  # Expect status 400 for invalid input

if __name__ == '__main__':
    unittest.main()
