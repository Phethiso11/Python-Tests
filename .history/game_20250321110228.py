import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Game")

# FPS
FPS = 60
clock = pygame.time.Clock()

# Colors (used for some UI or health bar)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets
player_img = pygame.image.load('./player.png')  # Replace with your own image path
enemy_img = pygame.image.load('./enemy.png')  # Replace with your own image path
background_img = pygame.image.load('./background.png')  # Replace with your own background path
bullet_img = pygame.Surface((5, 10))  # Bullet color (could be an image too)
bullet_img.fill((255, 0, 0))

# Setup Sprite Groups
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 50))  # Resize image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 50)
            self.rect.y = random.randint(-100, -40)

# Setup player
player = Player()
player_group.add(player)

# Game Loop
running = True
while running:
    screen.fill(BLACK)  # Clear screen

    # Draw background (scrolling effect)
    screen.blit(background_img, (0, 0))  # Draw background image

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullet_group.add(bullet)

    # Update game objects
    keys = pygame.key.get_pressed()
    player_group.update(keys)
    bullet_group.update()
    enemy_group.update()

    # Check bullet collision with enemies
    for bullet in bullet_group:
        collided_enemies = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for enemy in collided_enemies:
            bullet.kill()

    # Spawn new enemies
    if random.random() < 0.02:
        enemy = Enemy()
        enemy_group.add(enemy)

    # Draw sprites
    player_group.draw(screen)
    bullet_group.draw(screen)
    enemy_group.draw(screen)

    # Update display
    pygame.display.flip()

    # Control FPS
    clock.tick(FPS)

pygame.quit()
