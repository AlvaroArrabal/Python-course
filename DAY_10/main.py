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

background = pygame.image.load(".\\DAY_10\\background.png")

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
Enemy_pos_x_change = 0.2
Enemy_pos_y_change = 50

# bullet variables
bullet_icon = pygame.image.load(".\\DAY_10\\bullet.png")    # 64px
bullet_pos_x = 0
bullet_pos_y = 500
bullet_pos_x_change = 0
bullet_pos_y_change = 1
bullet_visible = False

# Player function
def player(x,y):
    screen.blit(player_icon,(x,y))

# Enemy function
def enemy(x,y):
    screen.blit(Enemy_icon,(x,y))

# shoot function
def shoot(x,y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_icon,(x+28,y+10))



# Game loop
running = True

while running:
    #screen.fill((46,30,134))              # RGB for the color of the screen
    # The order of the functions is very important
    screen.blit(background, (0,0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:       # when the user presses the "X" to close windows, the programme will close
            running = False

        if event.type == pygame.KEYDOWN:    # KEYDOWM, when the player press the key.
            if event.key == pygame.K_LEFT:
                player_pos_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_pos_change = 0.5
            if event.key == pygame.K_SPACE:
                shoot(player_pos_x,bullet_pos_y)

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
        Enemy_pos_x_change = 0.2
        Enemy_pos_y += Enemy_pos_y_change
    elif Enemy_pos_x >= 736:        # 800 - 64 = 736
        Enemy_pos_x_change = -0.2
        Enemy_pos_y += Enemy_pos_y_change
    player(player_pos_x,player_pos_y)
    enemy(Enemy_pos_x,Enemy_pos_y)

    # Bullet movement
    if bullet_visible:
        shoot(player_pos_x,bullet_pos_y)
        bullet_pos_y -= bullet_pos_y_change


    pygame.display.update()                 # update 

    