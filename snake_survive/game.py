try:  # pragma: no cover
    import pygame
except ModuleNotFoundError:  # pragma: no cover
    from . import pygame_stub as pygame

from .settings import WIDTH, HEIGHT, SEGMENT_SIZE
from .snake import Snake
from .fruit import Fruit
from .enemy import Enemy
from .weapon import BasicTurret


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake((WIDTH / 2, HEIGHT / 2))
    fruit = Fruit()
    turret = BasicTurret(snake)
    enemies = []
    score = 0
    enemy_spawn_timer = 0
    enemies_enabled = False

    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        snake.update(dt)

        if snake.head_rect().colliderect(
            pygame.Rect(fruit.position.x, fruit.position.y, SEGMENT_SIZE, SEGMENT_SIZE)
        ):
            snake.grow()
            score += 1
            fruit.respawn()
            enemies_enabled = True

        if enemies_enabled:
            enemy_spawn_timer -= dt
            if enemy_spawn_timer <= 0:
                enemies.append(Enemy())
                enemy_spawn_timer = max(0.5, 2 - score * 0.05)

        for enemy in enemies[:]:
            enemy.update(dt, snake.get_head_position())
            if enemy.hp <= 0:
                enemies.remove(enemy)
                continue
            if enemy.rect().colliderect(snake.head_rect()):
                snake.take_damage(10)
                enemy.hp = 0

        turret.update(dt, enemies)
        for bullet in turret.bullets:
            for enemy in enemies:
                if enemy.hp > 0 and bullet.rect().colliderect(enemy.rect()):
                    enemy.take_damage(10)
                    bullet.alive = False
                    break

        screen.fill((0, 0, 0))
        fruit.draw(screen)
        snake.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        turret.draw(screen)

        font = pygame.font.Font(None, 24)
        hp_text = font.render(f"HP: {int(snake.hp)}", True, (255, 255, 255))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(hp_text, (10, 10))
        screen.blit(score_text, (WIDTH - 120, 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
