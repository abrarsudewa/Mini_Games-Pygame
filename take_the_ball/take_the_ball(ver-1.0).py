'''
Take the ball ver 1.0
== WARNING ==
this game is a RAGE GAME that makes you angry and makes you destroys your computer.
^^^if you dont wants this happened to you just setting it the speed variabel that makes you angry.^^^

=== HOW TO PLAY ===
WASD or Arrow keys to move.
and the ball to get 1 point

dont touch the green dots, because its your enemy (and it always landing on the player position so dont stop moving).
take the ball to get 1 point score but if you die the score will be reduced by 2.
and dont forget if you jumpoff the score will be reduced by 2 and if you lives reached 0 GAMEOVER.

just like that thankyou ;) and sorry if my english is bad.
'''

import pygame, random, time
pygame.init()

# screen data
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Take the Ball ver 1.0")

# font score
score = 0
font_score = pygame.font.Font(None, 30)
lives = 3
font_lives = pygame.font.Font(None, 30)

# player data
speed_player = 0.3
x_player = 400
y_player = 250
radius_player = 10

# UP_enemy data (called "enemy1")
speed_enemy1 = 0.3
x_enemy1 = x_player
y_enemy1 = -10
radius_enemy1 = 10

# LEFT_enemy data (called "enemy2")
speed_enemy2 = 0.3
x_enemy2 = -10
y_enemy2 = y_player
radius_enemy2 = 10

# RIGHT_enemy data (called "enemy3")
speed_enemy3 = 0.3
x_enemy3 = 810
y_enemy3 = y_player
radius_enemy3 = 10

# DOWN_enemy data (called "enemy4")
speed_enemy4 = 0.3
x_enemy4 = x_player
y_enemy4 = -10
radius_enemy4 = 10

# ball data
x_ball = random.randint(10, 700)
y_ball = random.randint(10, 500)
radius_ball = 10

def reset_game():
    global x_player, y_player, x_enemy1, y_enemy1, x_enemy2, y_enemy2, x_enemy3, y_enemy3, x_enemy4, y_enemy4, x_ball, y_ball
    # reset the player position
    x_player = 400
    y_player = 250

    # reset the UP_enemy postition
    x_enemy1 = x_player
    y_enemy1 = -10

    # reset the LEFT_enemy position
    x_enemy2 = -10
    y_enemy2 = y_player

    # reset the RIGHT_enemy position
    x_enemy3 = 820
    y_enemy3 = y_player

    # reset the DOWN_enemy position
    x_enemy4 = x_player
    y_enemy4 = -10

    # reset the ball data position
    x_ball = random.randint(10, 700)
    y_ball = random.randint(10, 500)


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
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            reset_game()
            print("remember do not jump of the screen")
    if x_player <= -20:
        time.sleep(0.2)
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            reset_game()
            print("remember do not jump of the screen")
    if y_player >= screen_height+20:
        time.sleep(0.2)
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            reset_game()
            print("remember do not jump of the screen")
    if y_player <= -20:
        time.sleep(0.2)
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            reset_game()
            print("remember do not jump of the screen")

    """ Dram the objects """
    # UP_enemy
    UP_enemy = pygame.draw.circle(screen, (0, 255, 0), (x_enemy1, y_enemy1), radius_enemy1)
    y_enemy1 += speed_enemy1
    if y_enemy1 >= 520:
        y_enemy1 = -30
        x_enemy1 = x_player

    # DOWN_enemy
    DOWN_enemy = pygame.draw.circle(screen, (0, 255, 0), (x_enemy4, y_enemy4), radius_enemy4)
    y_enemy4 -= speed_enemy4
    if y_enemy4 <= -20:
        y_enemy4 = 530
        x_enemy4 = x_player

    # LEFT_enemy
    LEFT_enemy = pygame.draw.circle(screen, (0, 255, 0), (x_enemy2, y_enemy2), radius_enemy2)
    x_enemy2 += speed_enemy2
    if x_enemy2 > 820:
        x_enemy2 = -30
        y_enemy2 = y_player
    
    # RIGHT_enemy
    RIGHT_enemy = pygame.draw.circle(screen, (0, 255, 0), (x_enemy3, y_enemy3), radius_enemy3)
    x_enemy3 -= speed_enemy3
    if x_enemy3 < -20:
        x_enemy3 = 820
        y_enemy3 = y_player

    # Ball
    ball = pygame.draw.circle(screen, (255, 0, 0), (x_ball, y_ball), radius_ball)

    """Display the font"""
    # Update score text
    score_font = font_score.render(f"Score: {score}", True, (0, 0, 0))
    score_pos = score_font.get_rect(center=(45, 15))
    screen.blit(score_font, score_pos)

    # Update lives text
    lives_font = font_lives.render(f"Lives: {lives}", True, (255, 0, 0))
    lives_pos = lives_font.get_rect(center=(755, 15))
    screen.blit(lives_font, lives_pos)

    """ Colider """
    # when the player hit the ball
    if player.colliderect(ball):
        score += 1
        x_ball = random.randint(10, 700)
        y_ball = random.randint(10, 400)
        
    # if the player hit the UP_enemy
    if player.colliderect(UP_enemy):
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            time.sleep(0.2)
            reset_game()
            print("remember don't get hit by the enemy")

    # if the player hit the UP_enemy
    if player.colliderect(DOWN_enemy):
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            time.sleep(0.2)
            reset_game()
            print("remember don't get hit by the enemy")

    # if the player hit the DOWN_enemy
    if player.colliderect(LEFT_enemy):
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            time.sleep(0.2)
            reset_game()
            print("remember don't get hit by the enemy")

    # if the player hit the RIGHT_enemy
    if player.colliderect(RIGHT_enemy):
        lives -= 1
        if lives <= 0:
            time.sleep(0.5)
            running = False
            print("GAMEOVER, try again...")
        else:
            time.sleep(0.2)
            reset_game()
            print("remember don't get hit by the enemy")

    pygame.display.flip()

pygame.quit()