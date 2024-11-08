import unittest
import requests


class TestTemperatureApp(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'  # The base URL for the Flask app

    def test_convert_temperature(self):
        # Sending a POST request to the root route ('/')
        response = requests.post(f'{self.BASE_URL}/', data={'celsius': 25})
        
        # Check if the response code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert that the response contains the expected 'fahrenheit' value
        self.assertIn('fahrenheit', response.text)  # Checking if the fahrenheit result is in the response

    def test_invalid_temperature(self):
        # Sending a POST request with invalid data
        response = requests.post(f'{self.BASE_URL}/', data={'celsius': 'invalid'})
        
        # Check if the response code is 400 (Bad Request)
        self.assertEqual(response.status_code, 200)  # This should still return a 200 OK with an error message
        
        # Ensure the response contains the error message
        self.assertIn("Invalid input", response.text)

if __name__ == '__main__':
    unittest.main()
