import pygame, Objects, random, time
pygame.init()

FPS = 300
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 600])
pygame.display.set_caption("Flappy Bird version 0.0.0")

gravity = 1
x_Bird = 150
y_Bird = 250
player_speed = 1
jump_velocity = 2.5

pipe_x = 800
pipe_y = random.randint(-150, 100)
speed_pipe = 1.5
pipe_width = 50
pipe_height = 250

running = True
while running:

    clock.tick(FPS)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pipe_x -= speed_pipe # make the pipe keep moving to the right
    y_Bird += gravity # keep the bird fall by the gravity

    if pipe_x <= -100:
        pipe_x = 600
        pipe_y = random.randint(-150, 100)

    # if the bird press the SPACEBAR button then the bird will jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        y_Bird -= jump_velocity

    screen.fill((255, 255, 255)) # Fill the backgroud with White

    bird_rect = Objects.Bird(screen, (0, 0, 255), x_Bird, y_Bird, 10)
    top_pipe_rect, bottom_pipe_rect = Objects.Pipe(screen, (255, 0, 0), pipe_x, pipe_y, pipe_width, pipe_height)
    
    # Cek tabrakan dengan kedua pipa
    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
        time.sleep(1)  # Wait 1 Seconds before the Game close
        running = False
    
    pygame.display.flip()

pygame.quit()