import pygame, random
pygame.init()

clock = pygame.time.Clock()
FPS = 300

screen = pygame.display.set_mode([500, 500])

array_bomb = []

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # print("array_bomb itu sama dengan ini:",array_bomb)

    array_bomb.append([random.randint(20, 480), -10])
    # print(array_bomb)
            
    screen.fill((255, 255, 255))

    for bomb in array_bomb:
        bomb[1] += 1
        pygame.draw.circle(screen, (255, 0, 0), (bomb[0], bomb[1]), 10)

    array_bomb = [bomb for bomb in array_bomb if bomb[1] < 500]


    pygame.display.flip()

pygame.quit()