import pygame
import random

pygame.init()

HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

road = pygame.image.load("resources/AnimatedStreet.png")
coin_i = pygame.image.load("resources/Coin.png")
enemy_im = pygame.image.load("resources/Enemy.png")
player_im = pygame.image.load("resources/Player.png")

coin_im = pygame.transform.scale(coin_i, (50, 50))

pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound('resources/coin.mp3')
crash_sound = pygame.mixer.Sound('resources/crash.wav')

font = pygame.font.SysFont("Verdana", 30)
game_over_font = pygame.font.SysFont("Verdana", 50)

count = 0
game_over = False 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.generate() 

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.generate()

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.top = -self.rect.height

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

player = Player()
coin = Coin()
enemy = Enemy()

all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player.move()
        coin.move()
        enemy.move()

        if pygame.sprite.spritecollideany(player, coin_sprites):
            coin_sound.play()
            count += 1
            coin.generate()

        if pygame.sprite.spritecollideany(player, enemy_sprites):
            crash_sound.play()
            game_over = True  

    if game_over:
        screen.fill((255, 0, 0))  
        game_over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
    else:
        screen.blit(road, (0, 0))
        all_sprites.draw(screen)
        score_text = font.render(f"Score: {count}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()