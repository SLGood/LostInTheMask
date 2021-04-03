# LostInTheMask
Lost in the Mask 1802

import pygame
import math
import time
pygame.init()
screen=pygame.display.set_mode((640,480))
background=pygame.Surface(screen.get_size())
background.fill((255,255,255))
background.convert()
r = 255
g = 230
b = 200
rectx = 120
recty = 260
rect2x = 500
rect2y = 240
clock = pygame.time.Clock()
FPS=60
mainloop=True
dx=10
dy=2
while mainloop:
    clock.tick(FPS)
    screen.blit(background,(0,0))
    rectx = rectx + dx
    player = pygame.draw.rect(background,(0,g,0),(50,240,50,50))
    enemy = pygame.draw.rect(background,(r,0,b),(rect2x,rect2y,50,50))
    bullet = pygame.draw.circle(screen, (0,0,0), (rectx,recty),10)
    if bullet.colliderect(enemy):
        r=255
        b=0
        rectx=120
    else:
        r=0
        b=255
    pygame.display.flip()
time.sleep(10)
pygame.quit()
