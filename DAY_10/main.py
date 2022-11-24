import pygame


pygame.init()               # start the pygame

screen = pygame.display.set_mode((800, 600))        # (800,600) the size of the screen in pixels

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # when the user presses the "X" to close windows, the programme will close
            running = False
