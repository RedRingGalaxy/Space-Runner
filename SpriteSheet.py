import pygame

class SpriteSheet:

    sprite_sheet = None

    def __init__(self,filename):

        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_image(self,x,y,width,height):

        image = pygame.Surface([width,height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey((255,255,255))


        return image
    