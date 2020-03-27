import unittest

from Environment.Simple2DEnvironment import Simple2DEnvironment, Area
from Environment.Location.Location2D import Location2D
from TestUtil.DataProvider import DataProvider


class Simple2DEnvironmentTest(unittest.TestCase):
    def test_environment(self):
        env = Simple2DEnvironment(5, 5)
        self.assertEqual(env.xSize, 5)
        self.assertEqual(env.ySize, 5)

    @staticmethod
    def valid_locations():
        return (Location2D(-1, 2), False), \
               (Location2D(0, 0), True), \
               (Location2D(1, 2), True), \
               (Location2D(4, 2), True), \
               (Location2D(4, 4), True), \
               (Location2D(5, 4), False), \
               (Location2D(4, 5), False), \
               (Location2D(8, 6), False)

    @DataProvider("valid_locations")
    def test_valid_location(self, location, valid):
        env = Simple2DEnvironment(5, 5)
        self.assertEqual(env.is_valid_location(location), valid)

    def test_iterating(self):
        env = Simple2DEnvironment(5, 5)
        iterator = env.fuzzy_iter(2)
        self.assertEqual(next(iterator), Area(Location2D(0, 0), 2, 2))
        self.assertEqual(next(iterator), Area(Location2D(2, 0), 2, 2))
        self.assertEqual(next(iterator), Area(Location2D(4, 0), 1, 2))
        self.assertEqual(next(iterator), Area(Location2D(0, 2), 2, 2))
        self.assertEqual(next(iterator), Area(Location2D(2, 2), 2, 2))
        self.assertEqual(next(iterator), Area(Location2D(4, 2), 1, 2))
        self.assertEqual(next(iterator), Area(Location2D(0, 4), 2, 1))
        self.assertEqual(next(iterator), Area(Location2D(2, 4), 2, 1))
        self.assertEqual(next(iterator), Area(Location2D(4, 4), 1, 1))
        self.assertRaises(StopIteration, lambda: next(iterator))


if __name__ == '__main__':
    unittest.main()
