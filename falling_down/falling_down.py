# Just import time
import time
# Just import random
import random
# Import and initialize the pygame library
import pygame
pygame.init()

screen_width = 800 
screen_height = 500

# screen data
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Falling Down")

# player data
x_player = screen_width / 2 # position x player on the middle of screen
y_player = screen_height - 480 # position y player on the top of the screen
speed = 0.7 # player speed
extra_speed = 1
slow_speed = 0.1
gravity = 0.5 # player gravity

# square data
x_square = random.randint(100, 700) # random the x square position
y_square = screen_height - 30 # making the y square on 470
width_square = 100 # widht square
height_square = 20 # height square
random_x_square = random.randint(10, 450)
point = 0


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # make the player down and down and down to the HELL
    y_player = y_player + gravity

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y_player = y_player - slow_speed

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y_player = y_player + extra_speed

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x_player = x_player - speed

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x_player = x_player + speed

    
    
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle as the player
    circle = pygame.draw.circle(screen, (0, 0, 255), (x_player, y_player), 5)
    # Draw a square(landing point)
    square = pygame.draw.rect(screen, (0, 255, 0), (x_square, y_square, width_square, height_square))
    
    # when the player hit the square then
    if circle.colliderect(square):
        y_player = screen_height - 510 # set the y_player to -10
        x_player = random.randint(10,450)

    # changing the widht square(random) if the ball touching the green square
    if square.colliderect(circle): 
        width_square = random.randint(20,100)

    if circle.colliderect(square):
        x_square = random.randint(10, 450)
        time.sleep(1)
    
    if y_player > screen_height + 100:
        time.sleep(1)
        y_player = screen_height - 510
        x_player = screen_width / 2

    # Update the display
    pygame.display.flip()

