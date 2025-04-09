import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Call of Duty-like Shooter")

# FPS
FPS = 60
clock = pygame.time.Clock()

# Colors (for UI elements like health bar)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Load assets
player_img = pygame.image.load('./player.png')  # Replace with your own image path
enemy_img = pygame.image.load('./enemy.png')  # Replace with your own image path
bullet_img = pygame.Surface((10, 20))  # Bullet shape and size
bullet_img.fill((255, 0, 0))
background_img = pygame.image.load('./background.jpg')  # Replace with your own background path

# Setup Sprite Groups
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 50))  # Resize player image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5
        self.health = 100  # Player health

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Kill the player if health reaches 0

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 10

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)
        if self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 50))  # Resize enemy image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)
        self.health = 50  # Enemy health

    def update(self):
        # Move towards player
        player = player_group.sprites()[0] if player_group else None
        if player:
            direction = pygame.Vector2(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
            direction.normalize_ip()  # Normalize to unit vector
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

        # Reset if out of bounds
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 50)
            self.rect.y = random.randint(-100, -40)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Destroy enemy when health reaches 0

# Setup player
player = Player()
player_group.add(player)

# Score and Health Bars
font = pygame.font.SysFont('Arial', 24)
global score
score = 0

# Game Loop
running = True
while running:
    screen.fill(BLACK)  # Clear screen

    # Draw background
    screen.blit(background_img, (0, 0))  # Background image

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shooting angle calculation (based on mouse or direction of movement)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                player_x, player_y = player.rect.center
                angle = math.atan2(player_y - mouse_y, mouse_x - player_x)
                bullet = Bullet(player.rect.centerx, player.rect.top, angle)
                bullet_group.add(bullet)

    # Update game objects
    keys = pygame.key.get_pressed()
    player_group.update(keys)
    bullet_group.update()
    enemy_group.update()

    # Declare global score here to modify it

    
    # Check bullet collisions with enemies
    for bullet in bullet_group:
        collided_enemies = pygame.sprite.spritecollide(bullet, enemy_group, False)
        for enemy in collided_enemies:
            enemy.take_damage(20)
            bullet.kill()
            score += 1  # Increment score

    # Spawn new enemies
    if random.random() < 0.02:
        enemy = Enemy()
        enemy_group.add(enemy)

    # Draw sprites
    player_group.draw(screen)
    bullet_group.draw(screen)
    enemy_group.draw(screen)

    # Draw Health Bar (for player)
    pygame.draw.rect(screen, RED, (10, 10, 200, 20))  # Red background
    pygame.draw.rect(screen, GREEN, (10, 10, player.health * 2, 20))  # Green health bar

    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))

    # Update display
    pygame.display.flip()

    # Control FPS
    clock.tick(FPS)

pygame.quit()
