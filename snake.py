import pygame
import random

x = pygame.init()

VELOCITY = 3
SIZE = 20
food_size=15

velocity_x = 0
velocity_y = 0
# Game Display Window
gameWindow = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

snake_pos = pygame.Vector2(gameWindow.get_width() / 2, gameWindow.get_height() / 2)
food_pos = pygame.Vector2(random.randint(10, int(gameWindow.get_width() - 100)),
                          random.randint(10, int(gameWindow.get_height() - 100)))

font = pygame.font.SysFont(None, 50)

def text_screen(text, color, x, y):
    screen_print = font.render(text, True, color)
    gameWindow.blit(screen_print, (x, y))

dt = 0

# Game tracking variables
exit_game = False
game_over = False
score = 0
snake_list = []
snake_len = 1
paused = False
direction = "o"
run_game=False
def plot_body(gameWindow, color, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, SIZE, SIZE], SIZE)

# Button Properties
button_rect = pygame.Rect(150, 150, 200, 50)  # x, y, width, height
font = pygame.font.Font(None, 36)  # Default font, size 36
button_text = font.render("Start", True, "white")

while not exit_game:
    if not run_game:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Check if mouse is over button
        if button_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(gameWindow, "blue", button_rect)  # Darker color on hover
        else:
            pygame.draw.rect(gameWindow, "blue", button_rect)

        # Draw button text
        gameWindow.blit(button_text, (button_rect.x + 50, button_rect.y + 10))
        pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            if button_rect.collidepoint(event.pos):  # Check if clicked inside button
                print("Button Clicked!")
                run_game=True
    if run_game:
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                exit_game = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press 'P' to toggle pause
                    paused = not paused 
                    while paused:
                        gameWindow.fill("black")
                        text_screen("Game Paused", "white", gameWindow.get_width() / 2, gameWindow.get_height() / 2)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    paused = False
                
            # Border-collision
            if (snake_pos.x > 1000 or snake_pos.x < 0) or (snake_pos.y > 600 or snake_pos.y < 0):
                while not exit_game:
                        text_screen("Game Over", "red", gameWindow.get_width() / 2, gameWindow.get_height() / 2)
                        text_screen("Score : "+str(score),"black",gameWindow.get_width()/2,gameWindow.get_height()/2+50)
                        pygame.display.update()
                        pygame.time.delay(5000)
                        exit_game = True

        gameWindow.fill("white")

        pygame.draw.rect(gameWindow, "black", [snake_pos.x, snake_pos.y, SIZE, SIZE], SIZE)
        pygame.draw.rect(gameWindow, "red", [food_pos.x, food_pos.y, food_size, food_size], food_size)

        # Update Snake Body
        snake_head = (snake_pos.x, snake_pos.y)  # Get the current head position
        snake_list.append(snake_head)  # Add the new head position to the snake list

        # Maintain the length of the snake
        if len(snake_list) > snake_len:
            del snake_list[0]  # Remove the oldest segment if the snake is longer than its length


        # Maintain the length of the snake
        if len(snake_list) > snake_len:
            del snake_list[0]  # Remove the oldest segment if the snake is longer than its length

        # Food Creation
        if (abs(snake_pos.x - food_pos.x) < 10) and (abs(snake_pos.y - food_pos.y) < 10):
            food_pos = pygame.Vector2(random.randint(20, int(gameWindow.get_width() - 100)),
                                    random.randint(20, int(gameWindow.get_height() - 100)))
            pygame.draw.rect(gameWindow, "red", [food_pos.x, food_pos.y, SIZE, SIZE], SIZE)
            print("Score : " + str(score))

            score += 1
            snake_len += 5
            if score % 5 == 0 and VELOCITY < 10:  # Limit maximum speed
                VELOCITY += 1 # Increase the speed of the snake with every 7 points
            plot_body(gameWindow, "green", snake_list)

        #snake-body collision detection
        for (x, y) in snake_list[:-1]:
            if (x == snake_pos.x and y == snake_pos.y):
                game_over = True
                print("game over")
                if(game_over):
                    while not exit_game:
                        gameWindow.fill("white")
                        text_screen("Game Over", "red", gameWindow.get_width() / 2, gameWindow.get_height() / 2)
                        text_screen("Score : "+str(score),"black",gameWindow.get_width()/2,gameWindow.get_height()/2+50)
                        pygame.display.update()
                        pygame.time.delay(5000)
                        exit_game = True
                        
                    
                #delay exit by 5 seconds
                
        
            

        text_screen("Score : " + str(score), "black", 5, 5)
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and direction!="y"  : #Prevent movement in reverse direction
            velocity_y = -VELOCITY
            velocity_x = 0
            direction = "y"

        if keys[pygame.K_s] and direction!="y": #Prevent movement in reverse direction
            velocity_y = VELOCITY
            velocity_x = 0
            direction = "y"

        if keys[pygame.K_a] and direction!="x": #Prevent movement in reverse direction
            velocity_x = -VELOCITY
            velocity_y = 0
            direction = "x"

        if keys[pygame.K_d] and direction!="x": #Prevent movement in reverse direction
            velocity_x = VELOCITY
            velocity_y = 0
            direction = "x"

        snake_pos.x += velocity_x
        snake_pos.y += velocity_y

        plot_body(gameWindow, "green", snake_list)  # Draw the snake body

    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()
quit()
