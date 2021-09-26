######################
# Imports
######################
import pygame
import time
import random

#################################
# Configuring the Display & Game
#################################
pygame.init() # Initialize the pygame modules

white = (255, 255, 255) # define colours on RGB to be used by pygame.draw module
black=(0,0,0)
red=(255,0,0)
blue = (0,0,255)
green = (0, 255, 0)
yellow = (255, 255, 102)

dis_width = 400
dis_height = 300

dis = pygame.display.set_mode((dis_width,dis_height)) # configure display screen size
pygame.display.update() # Update game display based on changed config
pygame.display.set_caption('Snake Game Example') # Set game caption

clock = pygame.time.Clock() # pygame time tracker module
snake_block = 10 # snake block dimension
snake_speed = 10 # minimum speed of snake movement

##################################
# Message Output - General
##################################
font_style = pygame.font.SysFont("bahnschrift", 14) # set font style for general use case

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#############################################
# Snake - Create Snake of Interchangable size
#############################################
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) # rectangle dimension input = [left, top, width, height]


#############################################
# Score
#############################################

score_font = pygame.font.SysFont("comicsansms", 15) # set font style for score

def game_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

##################################
# Game
##################################

def snakeGame():
    game_active = True # Accounts for game being open and game running
    game_close = False # accounts for game being closed e.g. upon quitting
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

 
    while game_active:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            game_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_active = False
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_active = False
                        game_close = False
                    if event.key == pygame.K_c:
                        snakeGame()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snake(snake_block, snake_List)
        game_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
snakeGame()