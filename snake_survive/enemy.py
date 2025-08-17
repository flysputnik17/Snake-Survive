import random

try:  # pragma: no cover
    import pygame
except ModuleNotFoundError:  # pragma: no cover
    from . import pygame_stub as pygame

from .settings import WIDTH, HEIGHT, SEGMENT_SIZE


class Enemy:
    """Basic chaser enemy."""

    def __init__(self):
        self.position = pygame.Vector2(
            random.randint(0, WIDTH - SEGMENT_SIZE),
            random.randint(0, HEIGHT - SEGMENT_SIZE),
        )
        self.speed = 100
        self.hp = 10

    def update(self, dt, target):
        direction = target - self.position
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.position += direction * self.speed * dt

    def draw(self, surface):
        rect = pygame.Rect(self.position.x, self.position.y, SEGMENT_SIZE, SEGMENT_SIZE)
        pygame.draw.rect(surface, (255, 255, 0), rect)

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, SEGMENT_SIZE, SEGMENT_SIZE)

    def take_damage(self, amount):
        self.hp -= amount
