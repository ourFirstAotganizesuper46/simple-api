# import unittest

# from app import app
# import json

# class AppTestCase(unittest.TestCase):
#     def test_hello_with_string(self):
#         # test hello
#         res = app.hello("Rathachai")
#         self.assertEqual(res, "Hello, Rathachai")

#     def test_hello_with_number(self):
#         # test hello
#         res = app.hello(1)
#         self.assertEqual(res, "Hello, 1")
    
#     def test_plus_json(self):
#         res = app.plus(5,6)
#         self.assertEqual(json.loads(res.get_data()), {'result':11})

# if __name__ == "__main__":
#     unittest.main()

import unittest
from app import app
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client for Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_with_string(self):
        # Test hello route with a string
        res = self.app.get('/hello/Rathachai')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_data(as_text=True), "Hello, Rathachai")

    def test_hello_with_number(self):
        # Test hello route with a number
        res = self.app.get('/hello/1')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_data(as_text=True), "Hello, 1")
    
    def test_plus_json(self):
        # Test plus route with two numbers
        res = self.app.get('/plus/5/6')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.get_data(as_text=True)), {'result': 11})

if __name__ == "__main__":
    unittest.main()

