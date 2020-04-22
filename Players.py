import pygame
import SpriteSheet as ss

class Players(pygame.sprite.Sprite):

    change_y = 0

    pos = 0

    Alive =  True

    run_seq = []

    fall_speed = 1.9

    def __init__(self):

        super().__init__()

        sprite_sheet = ss.SpriteSheet("Run\\avatar2.png")

        avatar = sprite_sheet.get_image(5,3,69,102)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(80,3,58,102)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(141,3,54,102)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(205,3,41,102)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(249,7,49,96)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(299,7,68,96)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(368,10,66,95)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(7,111,56,97)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(69,111,51,97)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(133,114,42,94)
        self.run_seq.append(avatar)
        avatar = sprite_sheet.get_image(180,119,49,91)
        self.run_seq.append(avatar)

        self.image = self.run_seq[self.pos]

        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        
        if self.change_y == 0:
            nextpos = self.pos % len(self.run_seq)
            self.image = self.run_seq[int(nextpos)]
        else:
            self.change_y += self.fall_speed
            self.pos = 0 
            self.image = self.run_seq[self.pos]
            
        self.rect.y += self.change_y

    def jump(self):
        if self.change_y == 0:
            self.change_y = -12
            self.fall_speed = 0.4

    def fall(self):
        self.fall_speed = 5
        self.change_y = 1       



