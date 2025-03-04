"""
=== HOW TO PLAY ===
How to Play:
1. Main Objective:
- The player must jump from the red box and try to land right on the moving blue circle.

2. Controls:
- Press the Spacebar to make the player jump from the red box.

3. Blue Circle Movement (Arrow):
- The blue circle moves horizontally left and right at the bottom of the screen.
- The player must estimate the jump time in order to land right on the blue circle.

4. Winning Conditions:
- The player will win if he successfully lands on the red box first, then lands on the blue circle.
- After winning, the message "Hooray you Win!" will be displayed, and the game will reset after a few seconds.

5. Losing Conditions:
- If the player falls until the vertical position (y) reaches 520 or more, the player will lose.
- The message "You lose" will be displayed, and the game will reset after a few seconds.

Just like that :), sorry if my english is bad

"""

import pygame, time, random
pygame.init()

# screen data
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Ball_pit ver 0.0.0")

# fps variable
clock = pygame.time.Clock()
fps = 5000

# player variable
player_x = 700
player_y = 100
speed_player =  1
player_width = 20
player_height = 20
player_middle = player_width / 2
up = True
down = False
win = True

# arrow variable
x_arrow = 0
y_arrow = 350
speed_arrow = random.uniform(0.5,2)

# player bounce variable
right_arrow = True
left_arrow = False
moveRL = "enable"

# box variable
box_width = 80
box_height = 60
box_middle = box_width / 2
box_x_pos = random.randint(40, 760)

# platform wood
platform_width = 150
platform_height = 20
platform_middle = platform_width / 2

# fungtion reset game
def reset_game():
    global player_x, player_y, x_arrow, win, moveRL, up, down, right_arrow, left_arrow, speed_arrow, box_x_pos
    player_x = 700
    player_y = 100
    x_arrow = 0
    win = True
    moveRL = "enable"
    up = True
    down = False
    right_arrow = True
    left_arrow = False
    speed_arrow = random.uniform(0.5,2)
    box_x_pos = random.randint(40, 760)


# Game loop
running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background with white
    screen.fill((255, 255, 255))
    
    # check if the player press space bar then the player jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        moveRL = "disable"
    
    # moving the arrow to the right and left
    if moveRL == "enable":
        if right_arrow:
            if x_arrow < 780:
                x_arrow += speed_arrow
            if x_arrow >= 780:
                right_arrow = False
                left_arrow = True

        if left_arrow:
            if x_arrow > 0:
                x_arrow -= speed_arrow
            if x_arrow <= 0:
                right_arrow = True
                left_arrow = False

    # Mhen the player press space the player jump
    if moveRL == "disable":
        if up == True:
            player_y -= 1
        if player_y <= -300:
            up = False
            down = True
        if down == True:
            player_x = x_arrow
            player_y += 0.8

    # Drawing the player, arrow, box_collider  and platform
    platform = pygame.draw.rect(screen, (245, 200, 10), pygame.Rect(755 - platform_middle, 120, platform_width, platform_height))
    player = pygame.draw.rect(screen, (255, 100, 255), pygame.Rect(player_x - player_middle, player_y, player_width, player_height))
    arrow = pygame.draw.circle(screen, (0, 0, 255), (x_arrow, y_arrow), 10)
    box = pygame.draw.rect(screen, (153, 105, 9), pygame.Rect(box_x_pos - box_middle, 440, box_width, box_height))

    # Check if the player hit the box collider
    if player.colliderect(box):
        if win == True:
            print("Horay you Win!")
            win = False
            time.sleep(2)
            reset_game()
    if player_y >= 520:
        print("Bruh you lose, try again")
        time.sleep(2)
        reset_game()

    # Update the display
    pygame.display.flip()

pygame.quit()