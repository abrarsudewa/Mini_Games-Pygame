import pygame, random
pygame.init()

# Display setup
display = pygame.display.set_mode([500, 500])

# Fps setup
FPS = 60
clock = pygame.time.Clock()

# Time setup
delay_pipe = 1000
last_spawn_pipe = 0

JUMPING = False
gravity = 1
y_velocity = 10
x_bird_position, y_bird_position = 200, 250

def bird(x, y):
    pygame.draw.circle(display, (0, 0, 255), (x, y), 10)

pipe_speed = 3
x_pipe_position, y_pipe_position = 700, random.randint(200, 450)
array_pipe = []

run_game = True
while run_game:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    # Spawn pipe
    if current_time - last_spawn_pipe > delay_pipe:
        array_pipe.append([x_pipe_position, random.randint(200, 450)])
        last_spawn_pipe = current_time  # Update spawn time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    # Making the bird fall due to gravity
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_SPACE]:
        JUMPING = True
        y_velocity = 10
    if JUMPING:
        y_bird_position -= y_velocity
        y_velocity -= gravity

    display.fill((255, 255, 255))

    # Draw pipes and check collisions
    bird_collider = pygame.Rect(x_bird_position - 10, y_bird_position - 10, 20, 20)
    for pipes in array_pipe:
        pipes[0] -= pipe_speed
        pipe_collider = pygame.Rect(pipes[0], pipes[1], 80, 500)
        pygame.draw.rect(display, (0, 255, 0), pipe_collider)

        # Check collision with bird
        if bird_collider.colliderect(pipe_collider):
            run_game = False

    # Remove pipes that have moved off-screen
    array_pipe = [pipes for pipes in array_pipe if pipes[0] > -80]

    # Draw bird
    bird(x_bird_position, y_bird_position)

    pygame.display.flip()

pygame.quit()
