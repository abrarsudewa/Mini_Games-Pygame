import pygame

def Bird(screen, color, x, y, radius):
    return pygame.draw.circle(screen, (color), (x, y), radius)

pipe_gap = 400
def Pipe(screen, color, x, y, widht, height):
    top_pipe = pygame.draw.rect(screen, color, pygame.Rect(x, y - 120, widht, height+150))
    bottom_pipe = pygame.draw.rect(screen, color, pygame.Rect(x, y + pipe_gap, widht, height+150))
    return top_pipe, bottom_pipe