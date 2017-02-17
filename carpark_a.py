import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Car(object):
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def direction(self):
        angle = random.randint(0, 7)
        #north
        if angle == 0:
            self.speed_y = -5
            self.speed_x = 0
        #east
        elif angle == 1:
            self.speed_x = 5
            self.speed_y = 0
        #south
        elif angle == 2:
            self.speed_y = 5
            self.speed_x = 0
        #west
        elif angle == 3:
            self.speed_x = -5
            self.speed_y = 0
        #northeast
        elif angle == 4:
            self.speed_x = 5
            self.speed_y = -5
        #northwest
        elif angle == 5:
            self.speed_x = -5
            self.speed_y = -5
        #southeast
        elif angle == 6:
            self.speed_x = 5
            self.speed_y = 5
        #southwest
        elif angle == 7:
            self.speed_x = -5
            self.speed_y = -5
class Car1(Car):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0

car1 = Car1()

def main():

    width = 960
    height = 688
    #Initialize pygame and Display
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Carpark Game')
    clock = pygame.time.Clock()



    # GAME INITIALIZATION


    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            #keybindings
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down

                if event.key == KEY_DOWN:
                    car1.speed_y = 10
                elif event.key == KEY_UP:
                    car1.speed_y = -10
                elif event.key == KEY_LEFT:
                    car1.speed_x = -10
                elif event.key == KEY_RIGHT:
                    car1.speed_x = 10
            #more keybindings
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released

                if event.key == KEY_DOWN:
                    car1.speed_y = 0
                elif event.key == KEY_UP:
                    car1.speed_y = 0
                elif event.key == KEY_LEFT:
                    car1.speed_x = 0
                elif event.key == KEY_RIGHT:
                    car1.speed_x = 0

            #ends the game
            if event.type == pygame.QUIT:
                stop_game = True

                #location and speed of car
        car1.x += car1.speed_x
        car1.y += car1.speed_y

        #DISPLAY
        #loads background and picture of car
        background_image = pygame.image.load('parking_lot.png').convert_alpha()
        redv_image = pygame.image.load ('redv.png').convert_alpha()

        #draws backgound image and car based on x and y

        screen.blit(background_image, (0, 0))
        screen.blit(background_image, (0, 0))
        screen.blit(background_image, (0, 0))
        screen.blit(redv_image, (car1.x,car1.y))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    #quits pygame
    pygame.quit()

if __name__ == '__main__':
    main()
