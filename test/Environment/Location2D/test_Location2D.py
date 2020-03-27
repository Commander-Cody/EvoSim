import unittest

from Environment.Location.Location2D import Location2D


class MyTestCase(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Location2D(2, 3), Location2D(2, 3))
        self.assertNotEqual(Location2D(2, 3), Location2D(2, 4))
        self.assertNotEqual(Location2D(2, 3), 1)


if __name__ == '__main__':
    unittest.main()
