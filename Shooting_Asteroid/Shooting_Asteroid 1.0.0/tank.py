import pygame

def tank(screen, color, x_tank, y_tank, widht, height):
    # Drawing the tank as the player
    pygame.draw.rect(screen, (22, 94, 0), pygame.Rect(x_tank, y_tank, widht, height))
    pygame.draw.rect(screen, (22, 94, 0), pygame.Rect(x_tank + 5, y_tank - 5, widht - 10, height))
    # Making the tank barrel
    pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(x_tank + 28, y_tank - 20, widht - 55, height))
        