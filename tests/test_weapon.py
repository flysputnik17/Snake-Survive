import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    import pygame
except ModuleNotFoundError:  # pragma: no cover - use stub for headless tests
    from snake_survive import pygame_stub as pygame

from snake_survive.snake import Snake
from snake_survive.enemy import Enemy
from snake_survive.weapon import BasicTurret


def test_turret_fires():
    pygame.init()
    snake = Snake((100, 100))
    turret = BasicTurret(snake, fire_rate=10)
    enemy = Enemy()
    enemy.position.update(150, 100)
    turret.update(0.2, [enemy])
    assert len(turret.bullets) > 0
