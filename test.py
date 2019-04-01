import unittest
from test2 import obj


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_input_a(self):
        self.assertEqual(obj.shortesttrip([0, 0, 70], [90, 0, 45], ["1 2", "0 2", "0 1"], 0, 1), 6283.185307179586)

    def test_input_b(self):
        self.assertEqual(obj.shortesttrip([0, 30, 60], [25, -130, 78], ["1 2", "0 2", "1 2"], 0, 0), 0.0)

    def test_input_c(self):
        self.assertEqual(obj.shortesttrip([0, 20, 55], [-20, 85, 42], ["1", "0", "0"], 0, 2), -1.0)

    def test_input_d(self):
        self.assertEqual(obj.shortesttrip([0, 0, 70], [90, 0, 45], ["2", "0 2", "0 1"], 0, 1), 10612.237799994255)

    def test_input_e(self):
        self.assertEqual(obj.shortesttrip([0, 0, 60], [80, 0, 45], ["1 2", "0 1", "0 1"], 0, 1), 5585.0536063818545)

    def test_input_f(self):
        self.assertEqual(obj.shortesttrip([0, 0, 70], [90, 0, 45], ["1 2", "0 2", "0 1"], 0, 1), 6283.185307179586)


if __name__ == '__main__':
    unittest.main()
