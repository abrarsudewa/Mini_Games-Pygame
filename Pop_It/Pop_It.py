import pygame, random
pygame.init()

# display setup
display_widht = 800
display_height = 500
display = pygame.display.set_mode([display_widht, display_height])
pygame.display.set_caption("Pop It!")
# Fps setup
FPS = 120
clock = pygame.time.Clock()

# Make the current time in miliseconds
last_spawn_time = 0
delay_bubble = 600

bubble_array = []

running = True
while running:

    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Check if any bubble is clicked
            for bubble in bubble_array:  # Loop on a copy of the list
                bubble_rect = pygame.Rect(bubble[0] - 10, bubble[1] - 10, 20, 20)  # Create Rect around bubble
                if bubble_rect.collidepoint(mouse_x, mouse_y):  # Check if mouse click is inside bubble
                    bubble_array.remove(bubble)  # Remove bubble if clicked

    if current_time - last_spawn_time > delay_bubble:
        bubble_array.append([random.randint(10, display_widht-10), random.randint(10, display_height-10)])
        last_spawn_time = current_time

    display.fill([255, 255, 255])

    # Drawing the Bubble
    for bubble in bubble_array:
        pygame.draw.circle(display, (255, 0, 0), (bubble[0], bubble[1]), 10)

    pygame.display.flip()

pygame.quit()