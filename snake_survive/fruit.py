import random

try:  # pragma: no cover
    import pygame
except ModuleNotFoundError:  # pragma: no cover
    from . import pygame_stub as pygame

from .settings import WIDTH, HEIGHT, SEGMENT_SIZE


class Fruit:
    """Collectible fruit that grows the snake."""

    def __init__(self):
        self.position = self._random_position()

    def _random_position(self):
        return pygame.Vector2(
            random.randint(0, WIDTH - SEGMENT_SIZE),
            random.randint(0, HEIGHT - SEGMENT_SIZE),
        )

    def draw(self, surface):
        rect = pygame.Rect(self.position.x, self.position.y, SEGMENT_SIZE, SEGMENT_SIZE)
        pygame.draw.rect(surface, (255, 0, 0), rect)

    def respawn(self):
        self.position = self._random_position()
