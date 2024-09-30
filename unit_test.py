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
    
    def test_plus_json(self):
        res = app.plus(5,6)
        self.assertEqual(res['result'], 11)

    def test_true_when_x_is_17(self):
        res = app.is_prime(17)
        self.assertEqual(res, True)
    
    def test_false_when_x_is_36(self):
        res = app.is_prime(36)
        self.assertEqual(res, False)

    def test_true_when_x_is_13219(self):
        res = app.is_prime(13219)
        self.assertEqual(res, True)
    

if __name__ == "__main__":
    unittest.main()


