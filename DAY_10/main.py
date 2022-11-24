import pygame


# Initialise pygame
pygame.init()               

# Create the screen
screen = pygame.display.set_mode((800, 600))        # (800,600) the size of the screen in pixels


# Title and icon

pygame.display.set_caption("Alvaro's Game")         # Sets the title of the programme
icon = pygame.image.load(".\\DAY_10\\smiley.png")   # load the icon we want. In 32px!

pygame.display.set_icon(icon)                       # Sets the icon of the programme

running = True

player_icon = pygame.image.load(".\\DAY_10\\spacecraft.png")    # 64px
player_pos_x = 368            # 800/2 = 400 - 64/2 = 368
player_pos_y = 536            # 600-64 = 536
player_pos_change = 0

def player(x,y):
    screen.blit(player_icon,(x,y))

while running:
    screen.fill((205,144,228))              # RGB for the color of the screen
    # The order of the functions is very important
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # when the user presses the "X" to close windows, the programme will close
            running = False

        if event.type == pygame.KEYDOWN:    # KEYDOWM, when the player press the key. KEYUP when the player releases the key
            if event.key == pygame.K_LEFT:
                player_pos_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_pos_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_pos_change = 0
            if event.key == pygame.K_RIGHT:
                player_pos_change = 0
    
    player_pos_x += player_pos_change
    player(player_pos_x,player_pos_y)


    pygame.display.update()                 # update 

    