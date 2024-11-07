import unittest
import requests

class TestTemperatureApp(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'  

    def test_convert_temperature(self):

        response = requests.post(f'{self.BASE_URL}/convert', data={'celsius': 25})
        self.assertEqual(response.status_code, 200)
        self.assertIn('fahrenheit', response.json())  

    def test_invalid_temperature(self):
        
        response = requests.post(f'{self.BASE_URL}/convert', data={'celsius': 'invalid'})
        self.assertEqual(response.status_code, 400)  
        
if __name__ == '__main__':
    unittest.main()
