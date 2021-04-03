import pygame
pygame.init()

## example character class for mask switching
class Character(object):
    def __init__(self, mask):
        self.mask = mask

me = Character("Jock")
## maskInventory = ["Jock","Theater","Skater","Nerd","Band"]
## maskInventory[0] = "Jock"
## if maskInventory[0] == "Jock" then Good! else Bad!

win_dim = (400, 400)
win = pygame.display.set_mode(win_dim)
maskInventory = ["Jock", "Theater", "Skater", "Nerd", "Band"]
clock = pygame.time.Clock()
done = False
pause = False

while not done:

    deltaTime = clock.tick() / 1000

    gameEvent = pygame.event.get()
    keyPress = pygame.key.get_pressed()

    for event in gameEvent:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause = not pause
        elif event.type == pygame.QUIT:
            done = True

        if pause and event.type == pygame.KEYDOWN:
            if (event.key) == pygame.K_1:
                me.Mask = maskInventory[0]
                print(me.Mask)
            elif (event.key) == pygame.K_2:
                me.Mask = maskInventory[1]
                print(me.Mask)
            elif (event.key) == pygame.K_3:
                me.Mask = maskInventory[2]
                print(me.Mask)
            elif (event.key) == pygame.K_4:
                me.Mask = maskInventory[3]
                print(me.Mask)
            elif (event.key) == pygame.K_5:
                me.Mask = maskInventory[4]
                print(me.Mask)

    pygame.display.flip()


pygame.quit()