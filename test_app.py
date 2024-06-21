import unittest
import requests

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000/data"

    def test_get_data_response_time(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertLess(response.elapsed.total_seconds(), 1, "Response time is greater than 1 second")

    def test_get_data_content(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertIn("timestamp", data)
        self.assertIsInstance(data["timestamp"], float)
        self.assertEqual(data["message"], "Hello, this is your data!")

if __name__ == '__main__':
    unittest.main()
