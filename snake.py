import pygame
x = pygame.init()

VELOCITY = 5
#Game Display Window
gameWindow = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

car_pos = pygame.Vector2(gameWindow.get_width() / 2, gameWindow.get_height() / 2)
dt = 0

#Game tracking variables
exit_game = False
game_over = False


while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

    car_pos.x += VELOCITY

    gameWindow.fill("white")
                
    pygame.draw.rect(gameWindow,"red",[car_pos.x,car_pos.y,40,40],40)

    border_x = gameWindow.get_width()
    border_y = gameWindow.get_height()

    keys = pygame.key.get_pressed()

    player_speed = 250 * dt

    if keys[pygame.K_w]:
        car_pos.y -= player_speed
    if keys[pygame.K_s]:
        car_pos.y += player_speed
    if keys[pygame.K_a]:
        car_pos.x -= player_speed
    if keys[pygame.K_d]:
        car_pos.x += player_speed

    pygame.display.flip()

    dt = clock.tick(60)/1000


pygame.quit()
quit()
exit()