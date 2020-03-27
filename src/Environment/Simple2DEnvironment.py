from Environment.Location.Location2D import Location2D
from Util.RandomUtilities import get_random_positive_int


class Simple2DEnvironment:
    def __init__(self, x_size: int, y_size: int):
        # range: 0, x_size-1
        self.xSize = x_size
        self.ySize = y_size
        self.specialPoints = {}

    def generate(self):
        pass

    def is_obstructed(self, location):
        if location.get_coordinates() in self.specialPoints:
            return True
        return False

    def update(self):
        pass

    def fuzzy_iter(self, x, y=None):
        y = y or x
        return _Simple2DEnvironmentIterator(self, x, y)

    def is_valid_location(self, loc):
        return 0 <= loc.x < self.xSize and 0 <= loc.y < self.ySize


class _Simple2DEnvironmentIterator:
    def __init__(self, env, x, y):
        self.env = env
        self.x_size = x
        self.y_size = y
        self.x_iter = self.get_x_iterator()
        self.y_iter = self.get_y_iterator()
        self.current_loc: Location2D = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_loc is None:
            self.current_loc = Location2D(next(self.x_iter), next(self.y_iter))
        else:
            try:
                self.current_loc = Location2D(next(self.x_iter), self.current_loc.y)
            except StopIteration:
                self.x_iter = self.get_x_iterator()
                self.current_loc = Location2D(next(self.x_iter), next(self.y_iter))

        remaining_x = self.env.xSize - self.current_loc.x
        remaining_y = self.env.ySize - self.current_loc.y
        return Area(self.current_loc, min(self.x_size, remaining_x), min(self.y_size, remaining_y))

    def get_x_iterator(self):
        return iter(range(0, self.env.xSize, self.x_size))

    def get_y_iterator(self):
        return iter(range(0, self.env.ySize, self.y_size))


class Area:
    def __init__(self, loc, x_extent, y_extent):
        self.loc = loc
        self.x_extent = x_extent
        self.y_extent = y_extent

    def __eq__(self, other):
        if type(other) is type(self):
            return self.loc == other.loc and self.x_extent == other.x_extent and self.y_extent == other.y_extent
        return False

    def random_location(self):
        x_offset = get_random_positive_int(self.x_extent - 1)
        y_offset = get_random_positive_int(self.y_extent - 1)
        return self.loc.offset(x_offset, y_offset)
