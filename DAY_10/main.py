import pygame
import random
import math
from pygame import mixer

# Initialise pygame
pygame.init()               

# Create the screen
screen = pygame.display.set_mode((800, 600))        # (800,600) the size of the screen in pixels


# Title and icon

pygame.display.set_caption("X-Wing Attack")         # Sets the title of the programme

icon = pygame.image.load(".\\DAY_10\\smiley.png")   # load the icon we want. In 32px!
pygame.display.set_icon(icon)                       # Sets the icon of the programme

background = pygame.image.load(".\\DAY_10\\background.png")

# Music
mixer.music.load(".\\DAY_10\\backGroundMusic.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Player variables
player_icon = pygame.image.load(".\\DAY_10\\spacecraft.png")    # 64px
player_pos_x = 368            # 800/2 = 400 - 64/2 = 368
player_pos_y = 500            # 600-64 = 536
player_pos_change = 0

# Player function
def player(x,y):
    screen.blit(player_icon,(x,y))

# Enemy variables
Enemy_icon = []    # 64px
Enemy_pos_x = []
Enemy_pos_y = []
Enemy_pos_x_change = []
Enemy_pos_y_change = []
number_enemies = 8

for e in range(number_enemies):

    Enemy_icon.append(pygame.image.load(".\\DAY_10\\enemy.png"))   # 64px
    Enemy_pos_x.append(random.randint(0,736))
    Enemy_pos_y.append(random.randint(50,200))
    Enemy_pos_x_change.append(0.2)
    Enemy_pos_y_change.append(50)

# bullet variables
bullet_icon = pygame.image.load(".\\DAY_10\\bullet.png")    # 64px
bullet_pos_x = 0
bullet_pos_y = 500
bullet_pos_x_change = 0
bullet_pos_y_change = 1.5
bullet_visible = False

# score
score = 0
font = pygame.font.Font(".\\DAY_10\\256BYTES.ttf", 32)
text_x = 10
text_y = 10

# Game Over
finalFont = pygame.font.Font(".\\DAY_10\\256BYTES.ttf", 60)
def final_text():
    myFinalFont = finalFont.render("GAME OVER",True,(255,255,255))
    screen.blit(myFinalFont,(280,200))

# show score
def show_score(x,y):
    text = font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(text,(x,y))

# Player function
def player(x,y):
    screen.blit(player_icon,(x,y))

# Enemy function
def enemy(x,y,ene):
    screen.blit(Enemy_icon[ene],(x,y))

# shoot function
def shoot(x,y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_icon,(x+28,y+10))

# detecting collisions
def collision_check(x_1,y_1,x_2,y_2):
    distance = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_1-y_2,2))
    if distance < 27:
        return True
    else:
        return False


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
                shootEffect = mixer.Sound(".\\DAY_10\\shootEffect.mp3")
                shootEffect.play()
                if bullet_visible == False:
                    bullet_pos_x = player_pos_x
                    shoot(bullet_pos_x,bullet_pos_y)

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
    for e in range(number_enemies):
        # Game over
        if Enemy_pos_y[e] >500:
            for k in range(number_enemies):
                Enemy_pos_y[k] = 1000
            final_text()
            break

        Enemy_pos_x[e] += Enemy_pos_x_change[e]

        # Inside the screen - enemy
        if Enemy_pos_x[e] <= 0: 
            Enemy_pos_x_change[e] = 0.2
            Enemy_pos_y[e] += Enemy_pos_y_change[e]
        elif Enemy_pos_x[e] >= 736:        # 800 - 64 = 736
            Enemy_pos_x_change[e] = -0.2
            Enemy_pos_y[e] += Enemy_pos_y_change[e]
        # Collision
        collision = collision_check(Enemy_pos_x[e],Enemy_pos_y[e],bullet_pos_x,bullet_pos_y)
        if collision:
            collisionEffect = mixer.Sound(".\\DAY_10\\collisionEffect.mp3")
            collisionEffect.play()
            score += 1
            bullet_pos_y = 500
            bullet_visible = False
            Enemy_pos_x[e] = random.randint(0,736)
            Enemy_pos_y[e] = random.randint(50,200)
        
        enemy(Enemy_pos_x[e],Enemy_pos_y[e], e)


    # Bullet movement
    if bullet_pos_y <= -32:
        bullet_pos_y = 500
        bullet_visible = False
    if bullet_visible:
        shoot(bullet_pos_x,bullet_pos_y)
        bullet_pos_y -= bullet_pos_y_change


    player(player_pos_x,player_pos_y)
    show_score(text_x,text_y)

    pygame.display.update()                 # update 

    