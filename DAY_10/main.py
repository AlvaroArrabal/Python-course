import pygame
import random

# Initialise pygame
pygame.init()               

# Create the screen
screen = pygame.display.set_mode((800, 600))        # (800,600) the size of the screen in pixels


# Title and icon

pygame.display.set_caption("Alvaro's Game")         # Sets the title of the programme
icon = pygame.image.load(".\\DAY_10\\smiley.png")   # load the icon we want. In 32px!

pygame.display.set_icon(icon)                       # Sets the icon of the programme

running = True

# Player variables
player_icon = pygame.image.load(".\\DAY_10\\spacecraft.png")    # 64px
player_pos_x = 368            # 800/2 = 400 - 64/2 = 368
player_pos_y = 500            # 600-64 = 536
player_pos_change = 0

# Player function
def player(x,y):
    screen.blit(player_icon,(x,y))

# Enemy variables
Enemy_icon = pygame.image.load(".\\DAY_10\\enemy.png")    # 64px
Enemy_pos_x = random.randint(0,736)
Enemy_pos_y = random.randint(50,200)
Enemy_pos_x_change = 0.1
Enemy_pos_y_change = 50

# Player function
def player(x,y):
    screen.blit(player_icon,(x,y))

# Enemy function
def enemy(x,y):
    screen.blit(Enemy_icon,(x,y))

# Game loop
while running:
    screen.fill((46,30,134))              # RGB for the color of the screen
    # The order of the functions is very important

    for event in pygame.event.get():

        if event.type == pygame.QUIT:       # when the user presses the "X" to close windows, the programme will close
            running = False

        if event.type == pygame.KEYDOWN:    # KEYDOWM, when the player press the key.
            if event.key == pygame.K_LEFT:
                player_pos_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_pos_change = 0.3

        if event.type == pygame.KEYUP:      # KEYUP when the player releases the key
            if event.key == pygame.K_LEFT:
                player_pos_change = 0
            if event.key == pygame.K_RIGHT:
                player_pos_change = 0
    
    # Player movement
    player_pos_x += player_pos_change

    # Inside the screen - player
    if player_pos_x <= 0: 
        player_pos_x = 0
    elif player_pos_x >= 736:        # 800 - 64 = 736
        player_pos_x = 736

    # Enemy movement
    Enemy_pos_x += Enemy_pos_x_change

    # Inside the screen - enemy
    if Enemy_pos_x <= 0: 
        Enemy_pos_x_change = 0.1
        Enemy_pos_y += Enemy_pos_y_change
    elif Enemy_pos_x >= 736:        # 800 - 64 = 736
        Enemy_pos_x_change = -0.1
        Enemy_pos_y += Enemy_pos_y_change
    player(player_pos_x,player_pos_y)
    enemy(Enemy_pos_x,Enemy_pos_y)

    pygame.display.update()                 # update 

    