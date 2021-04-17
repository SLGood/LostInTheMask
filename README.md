# LostInTheMask
Lost in the Mask 1802


import pygame
import sys
import player
import box_collide


class Game:
    def __init__(self, surf, time):
        """The constructor"""
        self.surf = surf
        self.surf_dim = (1000, 750)
        self.world_dim = (5000, 750)
        self.player = player.Player(self)
        self.update_camera()
        self.time = time
        self.main_state = "Title"
        self.state = "House"
        self.normal_color = (175, 175, 175)
        self.highlight_color = (255, 255, 0)
        self.add_class()

    # GAME FUNCTIONS -- Functions not used in the main loop


    def add_class(self):
        """Add classes"""
        # TITLE STATE OBJECTS

        # Boxes -- boxes that can act as buttons
        self.start_box = box_collide.BoxCollideHidden(200, 450, 200, 20, self)
        self.quit_box = box_collide.BoxCollideHidden(200, 480, 200, 20, self)

        # Fonts -- fonts that are displayed on screen
        self.font_1 = pygame.font.SysFont("Courier New", 50)
        self.font_2 = pygame.font.SysFont("Courier New", 20)

        # GAME STATE OBJECTS

        # Boxes -- boxes that can act as the ground, wall, or ceiling
        self.house_box_1 = box_collide.BoxCollide(100, 100, 800, 550, (0, 0, 0), self)  # House box 1
        self.house_box_2 = box_collide.BoxCollide(0, 0, 1000, 750, (255, 255, 255), self)  # House box 2
        self.house_box_3 = box_collide.BoxCollide(100, 370, 800, 10, (255, 255, 255), self)  # House box 3

        self.school_box_1 = box_collide.BoxCollide(1000, 100, 3000, 550, (0, 0, 0), self)  # School box 1
        self.school_box_2 = box_collide.BoxCollide(900, 0, 3200, 750, (255, 255, 255), self)  # School box 2
        self.school_box_3 = box_collide.BoxCollide(1000, 370, 3000, 10, (255, 255, 255), self)  # School box 3

        # Invisible boxes -- special invisible boxes that serve a special purpose (can toggle invisibility)
        self.invis_box_1 = box_collide.BoxCollideHidden(600, 100, 300, 550, self)  # House invisible box
        self.invis_box_2 = box_collide.BoxCollideHidden(3500, 100, 500, 550, self)  # School invisible box

        # Ground -- the ground when state is equal to outside
        self.ground_1 = box_collide.BoxCollide(0, 650, 5000, 100, (0, 255, 0), self)  # Outside ground

        # Doors -- various doors the player can enter (depending on state)
        self.door_1 = box_collide.BoxCollide(200, 500, 100, 150, (255, 0, 0), self)  # House door
        self.door_2 = box_collide.BoxCollide(300, 500, 100, 150, (255, 0, 0), self)  # Outside house door
        self.door_3 = box_collide.BoxCollide(4500, 500, 100, 150, (255, 0, 0), self)  # Outside school door

        self.door_4 = box_collide.BoxCollide(2450, 500, 100, 150, (255, 0, 0), self)  # School door
        self.lunch_door = box_collide.BoxCollide(1450, 500, 100, 150, (255, 255, 0), self)
        self.gym_door = box_collide.BoxCollide(1950, 500, 100, 150, (255, 255, 0), self)
        self.math_door = box_collide.BoxCollide(2450, 220, 100, 150, (255, 255, 0), self)
        self.english_door = box_collide.BoxCollide(2950, 220, 100, 150, (255, 255, 0), self)
        self.band_door = box_collide.BoxCollide(3450, 220, 100, 150, (255, 255, 0), self)


    def draw_class(self):
        """Draw classes"""
        if self.main_state == "Title":
            # Draw text
            temps = self.font_1.render("LOST IN THE MASK", False, (255, 255, 255))
            self.surf.blit(temps, ((1000 / 10), (750 / 2)))
            temps = self.font_2.render("START GAME", False, self.normal_color)
            self.surf.blit(temps, (int(1000 / 5), 450))
            temps = self.font_2.render("QUIT GAME", False, self.normal_color)
            self.surf.blit(temps, (int(1000 / 5), 480))

        if self.main_state == "Game":
            # House state
            if self.state == "House":
                # Draw visible box
                self.house_box_2.draw()
                self.house_box_1.draw()
                self.house_box_3.draw()

                # Draw invisible box
                self.invis_box_1.draw()

                # Draw doors
                self.door_1.draw()

            # Outside state
            elif self.state == "Outside":
                # Draw ground
                self.ground_1.draw()

                # Draw doors
                self.door_2.draw()
                self.door_3.draw()

            # School state
            elif self.state == "School":
                # Draw visible box
                self.school_box_2.draw()
                self.school_box_1.draw()
                self.school_box_3.draw()

                # Draw invisible box
                self.invis_box_2.draw()

                # Draw doors
                self.door_4.draw()
                self.lunch_door.draw()
                self.gym_door.draw()
                self.math_door.draw()
                self.english_door.draw()
                self.band_door.draw()

            elif self.state == "Lunch":
                pass

            elif self.state == "Gym":
                pass

            elif self.state == "Math":
                pass

            elif self.state == "English":
                pass

            elif self.state == "Band":
                pass

            # Draw player
            self.player.draw()


    def update_camera(self):
        """Updates the camera position"""
        cam_x = self.player.pos[0] - self.surf_dim[0] / 2
        cam_y = self.player.pos[1] - self.surf_dim[1] / 2
        if cam_x < 0:
            cam_x = 0
        if cam_x > self.world_dim[0] - self.surf_dim[0]:
            cam_x = self.world_dim[0] - self.surf_dim[0]
        if cam_y < 0:
            cam_y = 0
        if cam_y > self.world_dim[1] - self.surf_dim[1]:
            cam_y = self.world_dim[1] - self.surf_dim[1]

        # Create / update the camera position
        self.camera_position = cam_x, cam_y

    def world_to_screen(self, world_position, to_int=True):
        """Converts the surface screen to the game world"""
        screen_x = world_position[0] - self.camera_position[0]
        screen_y = world_position[1] - self.camera_position[1]
        if to_int:
            screen_x = int(screen_x)
            screen_y = int(screen_y)

        return screen_x, screen_y


    # TITLE STATE


    def main_state_switch(self):
        """Switch main state"""
        # Title
        if self.main_state == "Title":
            if self.start_box.rect.width <= self.mousePos[0] <= (self.start_box.rect.width + 200) \
                    and (self.start_box.rect.height + 430) <= self.mousePos[1] <= (self.start_box.rect.height + 450):
                if self.mousePress[0]:
                    self.main_state = "Game"

            if self.start_box.rect.width <= self.mousePos[0] <= (self.start_box.rect.width + 200) \
                    and (self.start_box.rect.height + 460) <= self.mousePos[1] <= (self.start_box.rect.height + 480):
                if self.mousePress[0]:
                    pass
                    # pygame.quit()
                    # sys.exit()

        # Game
        elif self.main_state == "Game":
            self.state_switch()


    def draw_main_state(self):
        """Changes text color"""

        # self.start_box = box_collide.BoxCollideHidden(200, 450, 200, 20, self)
        # self.quit_box = box_collide.BoxCollideHidden(200, 480, 200, 20, self)

        if self.main_state == 'Title':
            # Start box
            if self.start_box.rect.width <= self.mousePos[0] <= (self.start_box.rect.width + 200) \
                    and (self.start_box.rect.height + 430) <= self.mousePos[1] <= (self.start_box.rect.height + 450):
                temps = self.font_2.render("START GAME", False, self.highlight_color)
                self.surf.blit(temps, (int(1000 / 5), 450))
            else:
                temps = self.font_2.render("START GAME", False, self.normal_color)
                self.surf.blit(temps, (int(1000 / 5), 450))

            # Quit box
            if self.start_box.rect.width <= self.mousePos[0] <= (self.start_box.rect.width + 200) \
                    and (self.start_box.rect.height + 460) <= self.mousePos[1] <= (self.start_box.rect.height + 480):
                temps = self.font_2.render("QUIT GAME", False, self.highlight_color)
                self.surf.blit(temps, (int(1000 / 5), 480))
            else:
                temps = self.font_2.render("QUIT GAME", False, self.normal_color)
                self.surf.blit(temps, (int(1000 / 5), 480))

    # GAME STATE


    def state_switch(self):
        """The state is house"""
        if self.state == "House":
            # Switch to outside state
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.door_1.rect.width + 100) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.door_1.rect.width + 200) and \
                    self.player.pos[1] >= (self.door_1.rect.height + 400):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.update_camera()
                        self.state = "Outside"

        # Outside doors
        elif self.state == "Outside":
            # Switch to house state
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.door_2.rect.width + 200) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.door_2.rect.width + 300) and \
                    self.player.pos[1] >= (self.door_2.rect.height + 400):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.state = "House"
            # Switch to school state
            elif self.player.pos[0] + (self.player.rect.width / 2) >= (self.door_3.rect.width + 4400) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.door_3.rect.width + 4500) and \
                    self.player.pos[1] >= (self.door_3.rect.height + 400):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.player.pos[0] = 2350
                        self.update_camera()
                        self.state = "School"

        # School doors
        elif self.state == "School":
            # Switch to outside state
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.door_4.rect.width + 2350) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.door_4.rect.width + 2450) and \
                    self.player.pos[1] >= (self.door_4.rect.height + 400):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.player.pos[0] = 4450
                        self.update_camera()
                        self.state = "Outside"

            # Lunch door
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.lunch_door.rect.width + 1350) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.lunch_door.rect.width + 1450) and \
                    self.player.pos[1] >= (self.lunch_door.rect.height + 400):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.state = "Lunch"

            # Gym door
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.gym_door.rect.width + 1850) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.gym_door.rect.width + 1950) and \
                    self.player.pos[1] >= (self.gym_door.rect.height + 400):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.state = "Gym"

            # Math door
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.math_door.rect.width + 2350) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.math_door.rect.width + 2450) and \
                    self.player.pos[1] <= (self.math_door.rect.height + 200):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.state = "Math"

            # English door
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.english_door.rect.width + 2850) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.english_door.rect.width + 2950) and \
                    self.player.pos[1] <= (self.english_door.rect.height + 200):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.state = "English"

            # Band door
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.band_door.rect.width + 3350) and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= (self.band_door.rect.width + 3450) and \
                    self.player.pos[1] <= (self.band_door.rect.height + 200):
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.state = "Band"

        elif self.state == "Lunch":
            pass

        elif self.state == "Gym":
            pass

        elif self.state == "Math":
            pass

        elif self.state == "English":
            pass

        elif self.state == "Band":
            pass


    def lunch_state(self):
        pass


    def gym_state(self):
        pass


    def math_state(self):
        pass


    def english_state(self):
        pass


    def band_state(self):
        pass


    def collision_detection(self):
        """Check for collision"""
        # State is house
        # Player stays in bounds 100 and 900 -- X
        # Player stays in bounds 100 and 650 -- Y
        if self.state == "House":
            # Box collision -- visible
            if self.player.pos[0] - (self.player.rect.width / 2) <= (self.house_box_1.rect.width - 700):
                self.player.pos[0] = (self.house_box_1.rect.width - 700) + (self.player.rect.width / 2)
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.house_box_1.rect.width + 100):
                self.player.pos[0] = (self.house_box_1.rect.width + 100) - (self.player.rect.width / 2)

            # Box collision -- invisible
            if self.player.pos[0] + (self.player.rect.width / 2) >= self.invis_box_1.rect.width + 300 and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= self.invis_box_1.rect.width + 600:
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        self.player.pos[1] = 605
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        self.player.pos[1] = 325

        # State is school
        # Player stays in bounds 1000 and 4000 -- X
        # Player stays in bounds 100 and 650 -- Y
        if self.state == "School":
            # Box collision -- visible
            if self.player.pos[0] - (self.player.rect.width / 2) <= (self.school_box_1.rect.width - 2000):
                self.player.pos[0] = (self.school_box_1.rect.width - 2000) + (self.player.rect.width / 2)
            if self.player.pos[0] + (self.player.rect.width / 2) >= (self.school_box_1.rect.width + 1000):
                self.player.pos[0] = (self.school_box_1.rect.width + 1000) - (self.player.rect.width / 2)

            # Box collision -- invisible
            if self.player.pos[0] + (self.player.rect.width / 2) >= self.invis_box_2.rect.width + 3000 and \
                    self.player.pos[0] - (self.player.rect.width / 2) <= self.invis_box_2.rect.width + 3500:
                for event in self.gameEvent:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        self.player.pos[1] = 605
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        self.player.pos[1] = 325


    # MAIN FUNCTIONS -- Functions in main loop


    def input(self, debug, event):
        """Detect user input"""
        self.keyPress = pygame.key.get_pressed()
        self.mousePos = pygame.mouse.get_pos()
        self.mousePress = pygame.mouse.get_pressed()
        self.debug = debug
        self.gameEvent = event
        self.player.input()

        # Climbing down stairs
        self.main_state_switch()
        if self.state == "Outside":
            self.update_camera()
        if self.state == "School":
            self.update_camera()


    def update(self):
        """Update our game"""
        # Time
        self.deltaTime = self.time.tick(60) / 1000

        # World collision
        world_area = (0, 0, 5000, 750)
        if self.player.pos[0] - (self.player.rect.width / 2) <= world_area[0]:
            self.player.pos[0] = world_area[0] + (self.player.rect.width / 2)
        if self.player.pos[0] + (self.player.rect.width / 2) >= world_area[0] + world_area[2]:
            self.player.pos[0] = world_area[0] + world_area[2] - (self.player.rect.width / 2)
        if self.player.pos[1] - (self.player.rect.height / 2) <= world_area[1]:
            self.player.pos[1] = world_area[1] + (self.player.rect.height / 2)
        if self.player.pos[1] + (self.player.rect.height / 2) >= world_area[1] + world_area[3]:
            self.player.pos[1] = world_area[1] + world_area[3] - (self.player.rect.height / 2)

        # State collision
        self.collision_detection()


    def draw(self):
        """Draw our game"""
        self.surf.fill((0, 0, 0))
        self.draw_class()
        self.draw_main_state()
        pygame.display.flip()
