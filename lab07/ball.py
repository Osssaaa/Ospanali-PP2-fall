import pygame

pygame.init()

width, height = 500, 500
white = (255, 255, 255)
red = (255, 0, 0)

ball_radius = 25
ball_speed = 20

ball_x = width // 2
ball_y = height // 2

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("moving ball")

running = True
while running:
    pygame.time.delay(50)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x - ball_radius - ball_speed >= 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + ball_speed <= width:
        ball_x += ball_speed
    if keys[pygame.K_UP] and ball_y - ball_radius - ball_speed >= 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius + ball_speed <= height:
        ball_y += ball_speed

    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    pygame.display.update()

pygame.quit()