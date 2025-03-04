import pygame

def car(screen, color, x, y, widht, height):
    pygame.draw.rect(screen, (color), pygame.Rect(x, y, widht+5, height+5))