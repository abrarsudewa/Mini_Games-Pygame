import pygame

def asteroids(screen, color, x_asteroids, y_asteroids, radius):
    # Drawing the tank as the player
    pygame.draw.circle(screen, color, (x_asteroids, y_asteroids), radius)