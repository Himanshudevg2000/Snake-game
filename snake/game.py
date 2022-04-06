import pygame
import random
import datetime

pygame.init()

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)

screen_height = 800
screen_width = 600
gameWindow = pygame.display.set_mode((screen_height,screen_width))

pygame.display.set_caption("Snake game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

FPS = 55

# def Game_Time(text,color,x,y):
#     screen_text = font.render(text,True, color)
#     gameWindow.blit(screen_text,[x,y])

def text_screen(text,color, x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake (gameWindow, color, snk_list,snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow,color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(blue)
        text_screen("Welcome to Snakes", white, 260, 250)
        text_screen("Press Space Bar To Play", white, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(60)

def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    score = 0
    init_velocity = 2
    GameTime = 0

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 170)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0


                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(black)
            text_screen("Score: " + str(score) + "HiScore: " + str(hiscore), red,100,0)
            # Game_Time("Time: " + str(GameTime * 1), blue,10,0)

            pygame.draw.rect(gameWindow,green, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)> snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>800 or snake_y<0 or snake_y>600:
                game_over = True

            if head in snk_list[:-1]:
                game_over = True

            plot_snake(gameWindow, white, snk_list,snake_size)
            
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit
    quit()
welcome()