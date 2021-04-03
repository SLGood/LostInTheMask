# LostInTheMask
Lost in the Mask 1802

import pygame
import math
import time
pygame.init()
screen=pygame.display.set_mode([640,480])
background=pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()
r = 255
g = 230
b = 200
circlex = 50
circley = 440
clock = pygame.time.Clock()
FPS=60
mainloop = True
dx = 10
dx2 = 20
while mainloop:
    clock.tick(FPS)
    screen.blit(background,(0,0))
    circlex = circlex + dx
    player=pygame.draw.circle(screen,(0,g,0),(circlex,circley),20)
    ladder=pygame.draw.rect(screen,(0,0,0),(400,50,10,400))
    if circlex >= 590:
        dx = -dx
    elif circlex <= 60:
        dx = -dx
    if player.colliderect(ladder):
        circley -= 3
        dx = 0
    else:
        circley -= 0
        dx = 10
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.flip()
pygame.quit()
