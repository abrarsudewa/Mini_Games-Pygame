import pygame
pygame.init()

# display setup
display_width = 800
display_height = 600
display = pygame.display.set_mode([display_width, display_height])

# FPS setup
clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self):
        self.x = 500
        self.y = 500

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x = 300
        if keys[pygame.K_d]:
            self.x = 500

    def draw(self):
        pygame.draw.circle(display, (0, 0, 255), (self.x, self.y), 10)

class Tree:
    def __init__(self):
        self.x = display_width // 2 # 800(display_width) // 2 the result is 400
        self.y = -300
        self.tree_width = 100
        self.middle_pos = self.tree_width // 2

    def move(self):
        self.y += 5

    def draw(self):
        pygame.draw.rect(display, (255, 0, 0), pygame.Rect(self.x - self.middle_pos, self.y, 100, 500))

player_obj = Player()
def player():
    player_obj.move()
    player_obj.draw()

tree_obj = Tree()
def tree():
    tree_obj.move()
    tree_obj.draw()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill((255, 255, 255))

    player()
    tree()

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()