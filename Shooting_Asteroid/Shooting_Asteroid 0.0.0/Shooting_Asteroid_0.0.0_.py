import random
import pygame, tank, enemy
pygame.init()

screen = pygame.display.set_mode([950, 600])
pygame.display.set_caption("Shooting Asteroid 0.0.0")
clock = pygame.time.Clock()
FPS = 300

bullet_array = []
asteroids_array = []

x_tank = 425
y_tank = 580
speed_tank = 2

speed_bullets = 3

shoot_delay = 200
last_shot_time = 0

asteroids_delay = 700
last_asteroids_time = 0
speed_asteroids = 0.3

running = True
while running:

    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    if current_time - last_asteroids_time > asteroids_delay:
        asteroids_array.append([random.randint(20, 930), -20])
        last_asteroids_time = current_time


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x_tank -= speed_tank
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x_tank += speed_tank

    # if the player press space then SHOT!
    if keys[pygame.K_SPACE] and current_time - last_shot_time >= shoot_delay:
        bullet_array.append([x_tank, y_tank])
        last_shot_time = current_time

    screen.fill((255, 255, 255))
    
    # Updating and drawing bullets
    for bullet in bullet_array[:]:
        bullet[1] -= speed_bullets
        pygame.draw.circle(screen, (0, 0, 255), (bullet[0] + 35, bullet[1] - 20), 7)
        
        if bullet[1] <= -20:
            bullet_array.remove(bullet)

    # Updating and drawing asteroids
    for asteroid in asteroids_array[:]:
        asteroid[1] += speed_asteroids
        enemy.asteroids(screen, (80, 80, 80), asteroid[0], asteroid[1], 20)

        # Check if asteroid has gone off screen
        if asteroid[1] >= 620:
            asteroids_array.remove(asteroid)

        # Collision detection
        for bullet in bullet_array[:]:
            if (
                asteroid[0] - 20 <= bullet[0] + 35 <= asteroid[0] + 20 and  # Check X-axis overlap
                asteroid[1] - 20 <= bullet[1] - 20 <= asteroid[1] + 20     # Check Y-axis overlap
               ):
                asteroids_array.remove(asteroid)
                bullet_array.remove(bullet)

    # Drawing the tank as the player
    tank.tank(screen, (0, 255, 0), x_tank, y_tank, 70, 15)

    pygame.display.flip()

pygame.quit()
