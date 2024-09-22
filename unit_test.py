import unittest

from app import app
import json

class AppTestCase(unittest.TestCase):
    def test_hello_with_string(self):
        # test hello
        res = app.hello("Rathachai")
        self.assertEqual(res, "Hello, Rathachai")

    def test_hello_with_number(self):
        # test hello
        res = app.hello(1)
        self.assertEqual(res, "Hello, 1")
    
    def test_plus_json(self):
        res = self.app.plus(5,6)
        self.assertEqual(json.loads(res.get_data()), {'result':11})

if __name__ == "__main__":
    unittest.main()
