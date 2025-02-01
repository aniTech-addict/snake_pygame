import pygame
import random

x = pygame.init()

VELOCITY = 3
SIZE = 10

velocity_x = 0
velocity_y = 0
#Game Display Window
gameWindow = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

car_pos = pygame.Vector2(gameWindow.get_width() / 2, gameWindow.get_height() / 2)
food_pos = pygame.Vector2(random.randint(10, int(gameWindow.get_width() -100 )),
                              random.randint(10, int(gameWindow.get_height()-100)))
dt = 0

#Game tracking variables
exit_game = False
game_over = False
score = 0


while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill("white")

    pygame.draw.rect(gameWindow,"green",[car_pos.x,car_pos.y,SIZE,SIZE],SIZE)
    pygame.draw.rect(gameWindow,"red",[food_pos.x,food_pos.y,SIZE,SIZE],SIZE)

    #Food Creation

    if (abs(car_pos.x - food_pos.x) < 2) and (abs(car_pos.y - food_pos.y) < 2):
        print("car_pos: ",car_pos.x, car_pos.y)
        print("food_pos: ",food_pos.x, food_pos.y)
        food_pos = pygame.Vector2(random.randint(20, int(gameWindow.get_width() -100)),random.randint(20, int(gameWindow.get_height() -100)))
        pygame.draw.rect(gameWindow, "red", [food_pos.x, food_pos.y, SIZE, SIZE], SIZE)
        print("Score : ", score)
        score += 1



    border_x = gameWindow.get_width()
    border_y = gameWindow.get_height()

    keys = pygame.key.get_pressed()

    player_speed = 250 * dt

    if keys[pygame.K_w]:
        velocity_y = -VELOCITY
        velocity_x = 0

    if keys[pygame.K_s]:
        velocity_y = VELOCITY
        velocity_x = 0

    if keys[pygame.K_a]:
        velocity_x = -VELOCITY
        velocity_y = 0

    if keys[pygame.K_d]:
        velocity_x = VELOCITY
        velocity_y = 0


    car_pos.x += velocity_x
    car_pos.y += velocity_y


    pygame.display.flip()

    dt = clock.tick(60)


pygame.quit()
quit()