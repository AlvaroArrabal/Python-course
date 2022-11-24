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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # when the user presses the "X" to close windows, the programme will close
            running = False
    screen.fill((205,144,228))              # RGB for the color of the screen
    pygame.display.update()                 # update 