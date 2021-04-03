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
circlex = 120
circley = 260
clock = pygame.time.Clock()
FPS=60
mainloop = True
sprint = False
dx = 10
dx2 = 20
while mainloop:
    clock.tick(FPS)
    screen.blit(background,(0,0))
    if sprint == True:
        circlex = circlex + dx * 2
        pygame.draw.circle(background,(0,0,b),(circlex,circley),20)
    circlex = circlex + dx
    pygame.draw.circle(screen,(0,g,0),(circlex,circley),20)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if sprint == False:
                    sprint = True
                elif sprint == True:
                    sprint = False
    if circlex >= 590:
        dx = -dx
    elif circlex <= 60:
        dx = -dx
    elif event.type == pygame.QUIT:
        mainloop = False   
    pygame.display.flip()
pygame.quit()
