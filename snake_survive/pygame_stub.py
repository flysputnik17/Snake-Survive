import math


class Vector2:
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        if isinstance(x, Vector2) and y == 0:
            x, y = x.x, x.y
        elif isinstance(x, (tuple, list)) and y == 0:
            x, y = x
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vector2(self.x * value, self.y * value)

    __rmul__ = __mul__

    def length_squared(self):
        return self.x * self.x + self.y * self.y

    def normalize(self):
        length = math.sqrt(self.length_squared())
        if length:
            return Vector2(self.x / length, self.y / length)
        return Vector2()

    def update(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def colliderect(self, other):
        return not (
            self.x + self.w < other.x
            or self.x > other.x + other.w
            or self.y + self.h < other.y
            or self.y > other.y + other.h
        )


# Dummy submodules and constants used by the game


def init():
    return ([], [])


def quit():
    pass


class font:
    class Font:
        def __init__(self, *args, **kwargs):
            pass

        def render(self, text, aa, color):
            return text


class draw:
    @staticmethod
    def rect(surface, color, rect):
        pass

    @staticmethod
    def circle(surface, color, position, radius):
        pass


class time:
    class Clock:
        def tick(self, fps):
            return 16


class display:
    @staticmethod
    def set_mode(size):
        return None

    @staticmethod
    def flip():
        pass


class event:
    @staticmethod
    def get():
        return []


class key:
    @staticmethod
    def get_pressed():
        return {}


K_LEFT = "left"
K_RIGHT = "right"
K_UP = "up"
K_DOWN = "down"
K_SPACE = "space"
QUIT = "quit"
