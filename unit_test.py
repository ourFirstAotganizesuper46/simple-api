import unittest

from app import app

class AppTestCase(unittest.TestCase):
    def test_hello_with_string(self):
        # test hello
        res = app.hello("Rathachai")
        self.assertEqual(res, "Hello, Rathachai")

    def test_hello_with_number(self):
        # test hello
        res = app.hello(1)
        self.assertEqual(res, "Hello, 1")
    
    def test_plus(self):
        # test plus
        res = app.plus(5, 6)
        self.assertEqual(res.result, 11)

if __name__ == "__main__":
    unittest.main()
