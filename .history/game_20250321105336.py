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
player_img = pygame.image.load('https://www.bing.com/images/search?view=detailV2&ccid=IVjpDBoM&id=23236B46C12691F991FBF13AFE23D37FC4C4D17C&thid=OIP.IVjpDBoMs9lIo1FNnbgTPQAAAA&mediaurl=https%3a%2f%2fwww.pngall.com%2fwp-content%2fuploads%2f5%2fPython-PNG-Free-Download-180x180.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.2158e90c1a0cb3d948a3514d9db8133d%3frik%3dfNHExH%252fTI%252f468Q%26pid%3dImgRaw%26r%3d0&exph=180&expw=180&q=player.png+pytohn&simid=608000119821004684&FORM=IRPRST&ck=32CEE4A2E02E0DA7DBA15FA04F43B6BC&selectedIndex=40&itb=1')  # Replace with your own image path
enemy_img = pygame.image.load('https://www.bing.com/images/search?view=detailV2&ccid=9ypXqA7V&id=C18E9ACB8494C0039F82890285A01D376146F58B&thid=OIP.9ypXqA7V886RZ3ZuTIYA1QHaJ4&mediaurl=https%3a%2f%2fih1.redbubble.net%2fimage.522897680.7990%2fflat%2c750x%2c075%2cf-pad%2c750x1000%2cf8f8f8.u8.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.f72a57a80ed5f3ce9167766e4c8600d5%3frik%3di%252fVGYTcdoIUCiQ%26pid%3dImgRaw%26r%3d0&exph=1000&expw=750&q=r+programming+logo&simid=608055228572251098&FORM=IRPRST&ck=27F073C7E7BC6DAF04A292763672E444&selectedIndex=2&itb=0')  # Replace with your own image path
background_img = pygame.image.load('https://www.bing.com/images/search?view=detailV2&ccid=in04XdOV&id=D959F96F54A44038B145622BDAA76749E0334BC0&thid=OIP.in04XdOVWCOVJCbZDmKYVgHaEo&mediaurl=https%3a%2f%2fwallpaperaccess.com%2ffull%2f3228833.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.8a7d385dd3955823952426d90e629856%3frik%3dwEsz4Elnp9orYg%26pid%3dImgRaw%26r%3d0&exph=1200&expw=1920&q=background.jpg&simid=608054129078790561&FORM=IRPRST&ck=21E0CF4BDB6CC979A6EA9193C3A8178D&selectedIndex=3&itb=0')  # Replace with your own background path
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
