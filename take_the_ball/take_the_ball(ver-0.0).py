'''
Take the ball ver 0.0
== WARNING ==
this game is a RAGE GAME that makes you angry and makes you destroys your computer.
^^^if you dont wants this happened to you just setting it the speed variabel that makes you angry.^^^

=== HOW TO PLAY ===
WASD or Arrow keys to move.

=== RULES ===
dont touch the green dots, becuz its your enemy (and it always landing on the player position so dont stop moving).
Take the ball for ... mmmm idk (i dont make the score because idk how lol)
and dont forget if you jumpoff the screen then GAMEOVER.

just like that thankyou ;) and sorry if my english is bad.
'''

import pygame, random, time
pygame.init()

# screen data
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Take the Ball ver 0.0")

# player data
speed_player = 0.4
x_player = 400
y_player = 250
radius_player = 15

# Yenemy data (called "enemy1")
speed_enemy2 = 0.5
x_enemy2 = -10
y_enemy2 = y_player
radius_enemy2 = 15

# Xenemy data (called "enemy1")
speed_enemy1 = 0.5
x_enemy1 = x_player
y_enemy1 = -10
radius_enemy1 = 15

# ball data
x_ball = random.randint(10, 700)
y_ball = random.randint(10, 500)
radius_ball = 15

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y_player -= speed_player
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y_player += speed_player
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x_player -= speed_player
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x_player += speed_player

    # fill the background with white
    screen.fill((255, 255, 255))

    # player
    player = pygame.draw.circle(screen, (0, 0, 255), (x_player, y_player), radius_player)
    # when the player jump off the screen
    if x_player >= screen_width+20:
        time.sleep(0.2)
        running = False
        print("remember do not jump of the screen")
    if x_player <= -20:
        time.sleep(0.2)
        running = False
        print("remember do not jump of the screen")
    if y_player >= screen_height+20:
        time.sleep(0.2)
        running = False
        print("remember do not jump of the screen")
    if y_player <= -20:
        time.sleep(0.2)
        running = False
        print("remember do not jump of the screen")

    # Y_enemy
    Y_enemy = pygame.draw.circle(screen, (0, 255, 0), (x_enemy1, y_enemy1), radius_enemy1)
    y_enemy1 += speed_enemy1
    if y_enemy1 >= 500:
        y_enemy1 = -10
        x_enemy1 = x_player

    # X_enemy
    X_enemy = pygame.draw.circle(screen, (0, 255, 0), (x_enemy2, y_enemy2), radius_enemy2)
    x_enemy2 += speed_enemy2
    if x_enemy2 > 800:
        x_enemy2 = -10
        y_enemy2 = y_player

    # Ball
    ball = pygame.draw.circle(screen, (255, 0, 0), (x_ball, y_ball), radius_ball)
    # when the player hit the ball
    if player.colliderect(ball):
        x_ball = random.randint(10, 700)
        y_ball = random.randint(10, 400)
    # if the player hit the Yenemy
    if player.colliderect(Y_enemy):
        time.sleep(0.2)
        running = False
        print("remember don't get hit by the enemy")
    # if the player hit the Xenemy
    if player.colliderect(X_enemy):
        time.sleep(0.2)
        running = False
        print("remember don't get hit by the enemy")

    pygame.display.flip()

pygame.quit()