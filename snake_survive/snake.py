try:  # pragma: no cover - fallback when pygame is unavailable
    import pygame
except ModuleNotFoundError:  # pragma: no cover - use lightweight stub
    from . import pygame_stub as pygame

from collections import deque
from .settings import SEGMENT_SIZE


class Snake:
    """Player-controlled snake."""

    def __init__(self, position, length=5):
        self.segment_size = SEGMENT_SIZE
        self.segments = deque([pygame.Vector2(position)])
        self.length = length
        self.direction = pygame.Vector2(1, 0)
        self.speed = 200  # pixels per second
        self.hp = 100
        self.max_hp = 100
        self.stamina = 100
        self.max_stamina = 100
        self.boost_multiplier = 2
        self.stamina_cost = 30

    def handle_input(self):
        keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)
        if keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_RIGHT]:
            move.x += 1
        if keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_DOWN]:
            move.y += 1
        if move.length_squared() > 0:
            move = move.normalize()
            self.direction = move

    def boost(self):
        if self.stamina >= self.stamina_cost:
            self.stamina -= self.stamina_cost
            return True
        return False

    def update(self, dt):
        self.handle_input()
        speed = self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.boost():
            speed *= self.boost_multiplier
        head = self.segments[0] + self.direction * speed * dt
        self.segments.appendleft(head)
        while len(self.segments) > self.length:
            self.segments.pop()
        # regenerate stamina
        self.stamina = min(self.max_stamina, self.stamina + 10 * dt)

    def draw(self, surface):
        for segment in self.segments:
            rect = pygame.Rect(segment.x, segment.y, self.segment_size, self.segment_size)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def grow(self, amount=1):
        self.length += amount

    def get_head_position(self):
        return self.segments[0]

    def head_rect(self):
        head = self.segments[0]
        return pygame.Rect(head.x, head.y, self.segment_size, self.segment_size)

    def take_damage(self, amount):
        self.hp -= amount
