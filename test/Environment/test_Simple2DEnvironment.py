import unittest

from Environment.Simple2DEnvironment import Simple2DEnvironment, Area
from Environment.Location.Location2D import Location2D


class Simple2DEnvironmentTest(unittest.TestCase):
    def test_environment(self):
        env = Simple2DEnvironment(5, 5)
        loc = Location2D(1, 2)
        self.assertEqual(env.is_obstructed(loc), False)

    def test_inaccessible_point(self):
        env = Simple2DEnvironment(5, 5)
        loc = Location2D(1, 2)
        env.specialPoints[loc.get_coordinates()] = True
        self.assertEqual(env.is_obstructed(loc), True)

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
