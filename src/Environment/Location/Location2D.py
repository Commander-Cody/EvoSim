class Location2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def __eq__(self, other):
        if type(other) is type(self):
            return self.x == other.x and self.y == other.y
        return False

    def offset(self, x, y):
        return Location2D(self.x + x, self.y + y)
