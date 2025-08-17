import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from snake_survive.snake import Snake


def test_snake_grow():
    snake = Snake((100, 100))
    initial_length = snake.length
    snake.grow()
    assert snake.length == initial_length + 1
