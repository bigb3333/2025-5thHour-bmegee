import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Basic Fortnite-like Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_velocity = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_velocity = 7

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_velocity = 3
enemies = []

# Set up font for scoring
font = pygame.font.SysFont('Arial', 24)

# Game loop flag
running = True

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((player_width, player_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x - player_velocity > 0:
            self.rect.x -= player_velocity
        if keys[pygame.K_RIGHT] and self.rect.x + player_velocity < SCREEN_WIDTH - player_width:
            self.rect.x += player_velocity

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= bullet_velocity
        if self.rect.y < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((enemy_width, enemy_height))
        self.image.fill((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - enemy_width)
        self.rect.y = random.randint(-150, -50)

    def update(self):
        self.rect.y += enemy_velocity
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, SCREEN_WIDTH - enemy_width)

# Initialize player and sprite groups
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
bullets = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Spawn initial enemies
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies_group.add(enemy)

# Game loop
while running:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shooting
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx - bullet_width // 2, player.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    # Update sprites
    all_sprites.update()

    # Check for collisions between bullets and enemies
    for bullet in bullets:
        hit_enemies = pygame.sprite.spritecollide(bullet, enemies_group, True)
        for hit in hit_enemies:
            bullet.kill()  # Remove bullet
            enemy = Enemy()  # Spawn a new enemy
            all_sprites.add(enemy)
            enemies_group.add(enemy)

    # Draw everything
    all_sprites.draw(screen)

    # Refresh display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
