try:  # pragma: no cover
    import pygame
except ModuleNotFoundError:  # pragma: no cover
    from . import pygame_stub as pygame

from .bullet import Bullet


class BasicTurret:
    """Simple auto-firing weapon."""

    def __init__(self, owner, fire_rate=1.0):
        self.owner = owner
        self.fire_rate = fire_rate
        self.cooldown = 0
        self.bullets = []

    def update(self, dt, enemies):
        self.cooldown -= dt
        target = self._find_target(enemies)
        if target and self.cooldown <= 0:
            self._fire(target)
            self.cooldown = 1.0 / self.fire_rate
        for bullet in self.bullets:
            bullet.update(dt)
        self.bullets = [b for b in self.bullets if b.alive]

    def _find_target(self, enemies):
        if not enemies:
            return None
        head = self.owner.get_head_position()
        return min(enemies, key=lambda e: (e.position - head).length_squared())

    def _fire(self, enemy):
        head = self.owner.get_head_position()
        direction = enemy.position - head
        bullet = Bullet(head, direction)
        self.bullets.append(bullet)

    def draw(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)
