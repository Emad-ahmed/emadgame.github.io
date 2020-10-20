import pygame
import random

x = pygame.init()

white = (255,55,88)
red =   (56,77,190)
kaki =  (145,167,189)

screen_width = 1200
screen_height = 600

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

exit_game = False
game_over = False
snake_x     = 45
snake_y     = 55
snake_size     = 20
velocity_x = 0
velocity_y = 0
food_x = random.randint(45, screen_width/2)
food_y = random.randint(45, screen_height/2)
score = 0
fps = 30
snk_list = []
snk_len = 1


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def textscreen(text,color, x,y):
    screen_text = font.render(text,True, color )
    game_window.blit(screen_text,[x,y])

def  plot_snake (game_window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x , y,snake_size, snake_size])





while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 5
                velocity_x = 0
            if event.key == pygame.K_UP:
                velocity_y = -5
                velocity_x = 0
            
    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=10
        food_x = random.randint(45, screen_width/2)
        food_y = random.randint(45, screen_height/2)
        snk_len += 5




    game_window.fill(red)
    textscreen("Score: "+str(score), kaki, 5, 5)
    pygame.draw.rect(game_window, kaki, [food_x,food_y, snake_size, snake_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_len:
        del snk_list[0]

    plot_snake(game_window, white, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()