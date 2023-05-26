import unittest
import functions


class TestAdd(unittest.TestCase):

    def test_add_0(self):
        expected = (0, 0)
        actual = functions.add((0, 0), (0, 0))
        self.assertEqual(expected, actual)

    def test_add_basic(self):

        actual1 = functions.add((1, 5), (3, 4))
        expected1 = (4, 9)
        self.assertEqual(expected1, actual1)

        actual2 = functions.add((23.9, 14.0), (7, 6.5))
        expected2 = (30.9, 20.5)
        self.assertEqual(actual2, expected2)


class TestMultiply(unittest.TestCase):
    def multiply_i_i(self):
        expected = (-1, 0)
        actual = functions.multiply((0, 1), (0, 1))
        self.assertEquals(expected, actual)
