import pygame
import SpriteSheet as ss

class Field_items(pygame.sprite.Sprite):

    speed = 0
    height = 0

    def __init__(self,item):

        super().__init__()

        sprite_sheet = ss.SpriteSheet("Run\\Fielditems.png")

        self.image = sprite_sheet.get_image(205,110,100,100)

        if item == 1:
            self.image = sprite_sheet.get_image(0,0,160,80)
        elif item == 2:
            self.image = sprite_sheet.get_image(195,0,150,100)
        elif item == 3:
            self.image = sprite_sheet.get_image(0,110,180,80)
        elif item == 4:
            self.image = sprite_sheet.get_image(0,220,140,80)
        elif item == 5:
            self.image = sprite_sheet.get_image(156,220,100,60)
        elif item == 6:
            self.image = sprite_sheet.get_image(0,330,60,90)
        elif item == 7:
            self.image = sprite_sheet.get_image(90,330,60,110)
        
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= self.speed
        self.rect.y = self.height



