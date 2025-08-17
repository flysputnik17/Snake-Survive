try:  # pragma: no cover
    import pygame
except ModuleNotFoundError:  # pragma: no cover
    from . import pygame_stub as pygame

from .settings import SEGMENT_SIZE


class Bullet:
    """Projectile fired by weapons."""

    def __init__(self, pos, direction, speed=400):
        self.position = pygame.Vector2(pos)
        self.direction = pygame.Vector2(direction)
        if self.direction.length_squared() != 0:
            self.direction = self.direction.normalize()
        else:
            self.direction = pygame.Vector2(1, 0)
        self.speed = speed
        self.radius = SEGMENT_SIZE // 4
        self.alive = True

    def update(self, dt):
        self.position += self.direction * self.speed * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius)

    def rect(self):
        return pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )
