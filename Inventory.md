# LostInTheMask
Lost in the Mask 1802

# MAIN LOOP

import pygame
import inventory


pygame.init()


win_dim = (800, 600)
win = pygame.display.set_mode(win_dim)
caption = pygame.display.set_caption("Inventory")
clock = pygame.time.Clock()
inv = inventory.Inventory(win)
slot_list = inv.create_slot(win)
done = False
pause = False

while not done:
    deltaTime = clock.tick() / 1000

    gameEvent = pygame.event.get()
    count = 0

    for event in gameEvent:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause = not pause
        inv.input(gameEvent, count)

    inv.draw(pause)

pygame.quit()


# INVENTORY CODE


import pygame


class Slot:
    """An individual slot in the inventory"""
    def __init__(self, x, y, surf, index):
        """The constructor"""
        self.pos = [x, y]
        self.surf = surf
        self.index = index
        self.normColor = (255, 255, 255)
        self.lightColor = (0, 255, 100)
        self.highlighted = False


    def draw_slots(self):
        """Draw the inventory slots"""
        if self.highlighted:
            pygame.draw.rect(self.surf, self.lightColor, (self.pos[0], self.pos[1], 100, 100), 1)
        else:
            pygame.draw.rect(self.surf, self.normColor, (self.pos[0], self.pos[1], 100, 100), 1)


class Inventory:
    """Simple inventory class"""
    def __init__(self, surf):
        """The constructor"""
        self.count = 5
        self.surf = surf


    def create_slot(self, surf):
        """Creates a slot"""
        slot_list = []
        x = 150
        y = 400
        for i in range(0, 5):
            slot_list.append(Slot(x, y, surf, i))
            x += 100

        return slot_list


    def input(self, event, count):
        """Detect user input"""
        self.gameEvent = event
        self.slot = self.create_slot(self.surf)
        self.count = count
        for evt in self.gameEvent:
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_1:
                self.slot[0].highlighted = not self.slot[0].highlighted
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_2:
                self.slot[1].highlighted = not self.slot[1].highlighted
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_3:
                self.slot[2].highlighted = not self.slot[2].highlighted
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_4:
                self.slot[3].highlighted = not self.slot[3].highlighted
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_5:
                self.slot[4].highlighted = not self.slot[4].highlighted


    def draw(self, pause):
        """Display objects"""
        self.surf.fill((100, 100, 100))
        if pause:
            pygame.draw.rect(self.surf, (0, 0, 0), (150, 400, 500, 100))
            for s in self.slot:
                s.draw_slots()
        pygame.display.flip()

