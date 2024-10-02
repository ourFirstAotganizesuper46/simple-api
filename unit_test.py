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
        self.assertEqual(res['result'], True)
    
    def test_false_when_x_is_36(self):
        res = app.is_prime(36)
        self.assertEqual(res['result'], False)

    def test_true_when_x_is_13219(self):
        res = app.is_prime(13219)
        self.assertEqual(res['result'], True)
    
    def test_true_when_x_is_3(self):
        res = app.is_fibonacci(3)
        self.assertEqual(res['result'], True)
    
    def test_false_when_x_is_4(self):
        res = app.is_fibonacci(4)
        self.assertEqual(res['result'], False)

    def test_false_when_x_is_5(self):
        res = app.is_fibonacci(5)
        self.assertEqual(res['result'], True)

    def test_x_is_1(self):
        res = app.next5(1)
        self.assertEqual(res['result'], 6)
    
    def test_x_is_neg10(self):
        res = app.next5(-10)
        self.assertEqual(res['result'], -5)

    def test_x_is_1dot5(self):
        res = app.next5(1.5)
        self.assertEqual(res['result'], 6.5)

if __name__ == "__main__":
    unittest.main()


