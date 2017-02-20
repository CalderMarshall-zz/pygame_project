import pygame
#set key numbers
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_S = 115

#create the class Car
class Car(object):
    def __init__(self, x, y, speed_x, speed_y,image):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.angle = 0
        self.init_image = image
        self.current_image = self.init_image

#main function
def main():

    width = 960
    height = 688
    #Initialize pygame and Display
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("swing.wav")
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((width, height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Carpark Game')
    clock = pygame.time.Clock()
    redv_image = pygame.image.load ('red_car.png').convert_alpha()
    bluev_image = pygame.image.load ('blue_car.png').convert_alpha()
    greenv_image = pygame.image.load ('green_car.png').convert_alpha()
    # num = 3
    control_cars = []

    # for i in xrange(num):
    #     control_cars.append(Car(546,250,0,0,redv_image))
#setting car objects and appedning to control_cars
    car1 = Car(546,57,0,0,redv_image)
    car2 = Car(15,52,0,0,bluev_image)
    car3 = Car(753,61,0,0,greenv_image)
    control_cars.append(car1)
    control_cars.append(car2)
    control_cars.append(car3)
    # GAME INITIALIZATION
    carpointer = 0
    stop_game = False
    while not stop_game:
        current = control_cars[carpointer]
        for event in pygame.event.get():
            # Event handling
            #keybindings
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_S:
                    if carpointer < len(control_cars) -1:
                        carpointer += 1
                    else:
                        carpointer = 0
                if event.key == KEY_DOWN:
                    if current.angle == 0:
                        current.speed_x = 0
                        current.speed_y = 11
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 90:
                        current.speed_x = 11
                        current.speed_y = 0
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 180:
                        current.speed_x = 0
                        current.speed_y = -11
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 270:
                        current.speed_y = 0
                        current.speed_x = -11
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 360:
                        current.speed_x = 0
                        current.speed_y = 11
                        print current.angle
                        print current.x
                        print current.y
                elif event.key == KEY_UP:
                    if current.angle == 0:
                        current.speed_x = 0
                        current.speed_y = -11
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 90:
                        current.speed_x = -11
                        current.speed_y = 0
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 180:
                        current.speed_x = 0
                        current.speed_y = 11
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 270:
                        current.speed_y = 0
                        current.speed_x = 11
                        print current.angle
                        print current.x
                        print current.y
                    elif current.angle == 360:
                        current.speed_x = 0
                        current.speed_y = -11
                        print current.angle
                        print current.x
                        print current.y
                elif event.key == KEY_LEFT:
                    current.angle += 90
                    if current.angle >= 360:
                        current.angle -= 360
                    print current.angle
                    print current.x
                    print current.y
                    current.current_image = pygame.transform.rotate(current.init_image, current.angle)
                elif event.key == KEY_RIGHT:
                    current.angle -= 90
                    if current.angle < 0:
                        current.angle += 360
                    print current.angle
                    print current.x
                    print current.y
                    current.current_image = pygame.transform.rotate(current.init_image, current.angle)

            #more keybindings
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released

                if event.key == KEY_DOWN:
                    current.speed_y = 0
                    current.speed_x = 0
                    print "down"
                elif event.key == KEY_UP:
                    current.speed_y = 0
                    current.speed_x = 0
                    print "up"
                elif event.key == KEY_LEFT:
                    current.speed_x = 0
                    current.speed_y = 0
                    print "left"
                elif event.key == KEY_RIGHT:
                    current.speed_x = 0
                    current.speed_y = 0
                    print "right"

            #ends the game
            if event.type == pygame.QUIT:
                stop_game = True

                #location and speed of car
        current.x += current.speed_x
        current.y += current.speed_y


        #DISPLAY
        #loads background and picture of car
        background_image = pygame.image.load('parking_lot.png').convert_alpha()



        #draws backgound image and car based on x and y

        screen.blit(background_image, (0, 0))
        screen.blit(background_image, (0, 0))
        screen.blit(background_image, (0, 0))
        # screen.blit(redv_image, (current.x,current.y))


        #screen blit for controlled cars
        for i in control_cars:
            screen.blit(i.current_image,(i.x, i.y))
        # screen.blit(image_rotated, (car2.x, car2.y))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(200)
    #quits pygame
    pygame.quit()

if __name__ == '__main__':
    main()
#FUNCTIONALITY TO ADD
    #COLLISON DETECTION BETWEEN CARS
    #PEDESTRIANS WITH RANDOM MOVEMENT AND COLLISON DETECTION
    #LOAD A CAR IN A HORIZONTAL SPOT, FACING THE CORRECT DIRECTION
