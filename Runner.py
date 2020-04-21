import pygame
import Constant
from Players import Players
import Fields
import random

def main():
    #Init pygame
    pygame.init()

    #Initialize display parameter
    screen = pygame.display.set_mode([Constant.DISPLAY_WIDTH, Constant.DISPLAY_HEIGHT])

    pygame.display.set_caption("Space Runner || Author : Thiru")

    screen.fill((255,255,255))

    start = GameInstruction(screen,"Press \"Space Bar\" to start the Game")

    while start:
        if not play(screen):
            break
    
def play(screen):
    
    
    done = False
    clock = pygame.time.Clock()

    previous_obstacle_loc = Constant.DISPLAY_WIDTH
    obstacles_speed = 5

    player = Players()
    player.rect.x = 0
    player.rect.y = Constant.DISPLAY_HEIGHT - player.rect.height

    active_items = pygame.sprite.Group()

    active_items.add(player)

    obstacles = pygame.sprite.Group()


    sky_list = pygame.sprite.Group()

    sun = Fields.Field_items(0)
    sun.rect.x = Constant.DISPLAY_WIDTH // 2
    sun.rect.y = 10
    sky_list.add(sun)

    cloud = Fields.Field_items(1)
    cloud.rect.x = Constant.DISPLAY_WIDTH // 2
    cloud.height = random.randint(0,20)
    cloud.speed = random.randint(2,10)
    sky_list.add(cloud)

    cloud = Fields.Field_items(2)
    cloud.rect.x = Constant.DISPLAY_WIDTH 
    cloud.height = random.randint(0,20)
    cloud.speed = random.randint(2,10)
    sky_list.add(cloud)

    cloud = Fields.Field_items(3)
    cloud.rect.x = 0
    cloud.height = random.randint(0,20)
    cloud.speed = random.randint(2,10)
    sky_list.add(cloud)


    fps = 60

    while not done:

        if player.Alive == False:
            done = True
            break

        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()

                if event.key == pygame.K_DOWN:
                    player.fall()

        player.pos += 0.5

        if Constant.DISPLAY_HEIGHT <  player.rect.y + player.rect.height:
            player.rect.y = Constant.DISPLAY_HEIGHT - player.rect.height
            player.change_y = 0


        if len(obstacles) < 6:
            previous_obstacle_loc += 500

            l = int(random.randrange(1,2,1))

            for i in range(l):
                itm = random.randint(4,7)
                obst = Fields.Field_items(itm)
                obst.rect.x = previous_obstacle_loc + 10
                obst.height = Constant.DISPLAY_HEIGHT - obst.rect.height
                obst.speed = obstacles_speed
                obstacles.add(obst)
                previous_obstacle_loc = obst.rect.x + obst.rect.width


        for item in sky_list:
            if item.rect.x + item.rect.width < 0:
                item.rect.x = Constant.DISPLAY_WIDTH
                item.height =int(random.randrange(0,100,10))
                item.speed = int(random.randrange(2,8,2))

        for item in obstacles:
            if item.rect.x + item.rect.width < 0:
                obstacles.remove(item)

        hit = pygame.sprite.spritecollide(player, obstacles, False)

        if len(hit) > 0:
            player.Alive = False
            done = True


        sky_list.update()
        active_items.update()
        obstacles.update()

        sky_list.draw(screen)
        active_items.draw(screen)
        obstacles.draw(screen)

        pygame.display.flip()

        clock.tick(fps)

    if player.Alive == False:
        return GameInstruction(screen,"Game Over")


    pygame.quit()


def GameInstruction(screen, Message):
    done = False
    accept = False
    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    accept = True
                    done = True

                if event.key == pygame.K_ESCAPE:
                    done = True

        font = pygame.font.Font('freesansbold.ttf', 32)  
        text = font.render(Message, True, (255,255,255), (0,0,0))
        textRect = text.get_rect()

        image = pygame.Surface([textRect.width + 100 , textRect.height + 100])
        image.fill((0,0,0))
        rect = image.get_rect()
        rect.center = (Constant.DISPLAY_WIDTH // 2,Constant.DISPLAY_HEIGHT // 2)

        textRect.center = rect.center

        screen.blit(image,rect)
        screen.blit(text,textRect)

        pygame.display.update()

    return accept


if __name__ == "__main__":
    main()