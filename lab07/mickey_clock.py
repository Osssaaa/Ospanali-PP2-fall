import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))

im1 = pygame.image.load(r"C:\\Users\\ospan\\OneDrive\\Рабочий стол\\PP2\\Ospanali-PP2-fall\\lab07\\images\\clock.png")
min_hand = pygame.image.load(r"C:\\Users\\ospan\\OneDrive\\Рабочий стол\\PP2\\Ospanali-PP2-fall\\lab07\\images\\min_hand.png")
sec_hand = pygame.image.load(r"C:\\Users\\ospan\\OneDrive\\Рабочий стол\\PP2\\Ospanali-PP2-fall\\lab07\\images\\sec_hand.png")

clock = pygame.time.Clock()

size_min = min_hand.get_rect()
size_sec = sec_hand.get_rect()

while True:
    screen.fill((255, 255, 255))
    screen.blit(im1, (0, 0))

    now = datetime.now()
    minute = now.minute  
    second = now.second
    diff_min = 50
    diff_sec = -53
    angle_min = -(minute * 6) - diff_min
    angle_sec = -(second * 6) - diff_sec

    rotated_min = pygame.transform.rotate(min_hand, angle_min)
    rotated_sec = pygame.transform.rotate(sec_hand, angle_sec)
    
    rotated_m = rotated_min.get_rect(center=(400, 300))  
    rotated_s = rotated_sec.get_rect(center=(400, 300))  

    screen.blit(rotated_min, rotated_m)
    screen.blit(rotated_sec, rotated_s)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  
    
    clock.tick(1)