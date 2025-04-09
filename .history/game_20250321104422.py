import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 50, 60
player_x, player_y = WIDTH // 2, HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width, bullet_height = 5, 10
bullet_speed = -7
bullets = []

# Enemy settings
enemy_width, enemy_height = 50, 50
enemy_speed = 3
enemies = []

# Font for score
font = pygame.font.SysFont("Arial", 24)

# Score
score = 0

# Game loop flag
running = True

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_bullet(bullets):
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, enemy)

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_width)
    y = random.randint(-100, -40)
    return pygame.Rect(x, y, enemy_width, enemy_height)

# Main game loop
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit the number of bullets on screen
            bullets.append(pygame.Rect(player_x + player_width // 2, player_y, bullet_width, bullet_height))

    # Update bullets
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, 50) == 1:  # Random chance to spawn an enemy
        enemies.append(spawn_enemy())

    # Update enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        # Check for collision with bullets
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1

    # Draw everything
    draw_player(player_x, player_y)
    draw_bullet(bullets)
    draw_enemies(enemies)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()