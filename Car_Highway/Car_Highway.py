import pygame, player_car  # Import Pygame and player_car module
import random  # Import random module
pygame.init()  # Initialize all Pygame modules

# Screen setup
screen_width = 800  # Width of the game screen
screen_height = 500  # Height of the game screen
screen = pygame.display.set_mode([screen_width, screen_height])  # Create the game screen
pygame.display.set_caption("Car Highway Racing")  # Set window title

# Fps setup
FPS = 120
clock = pygame.time.Clock()

# Player car data
x_car_player = 400  # Initial x position of player car
y_car_player = 400  # Initial y position of player car
width_car_player = 30  # Width of the player car
height_car_player = 50  # Height of the player car

speed_car_player = 5  # Default speed of the player car
middle_car_player = width_car_player / 2  # Center alignment of the player car

# Making the Center Line for the Road
center_line_road = []
speed_center_line_road = 5
last_time_center_line_road = 0
delay_center_line_road = 300

# Making the foreign vehicles
foreign_vehicles_array = []
speed_foreign_vehicles = 2
last_time_foreign_vehicles = 0
delay_foreign_vehicles = 500

speed = True
last_time_speed = 0
delay_speed = 5000

running = True  # Game loop control variable
while running:
    
    current_time = pygame.time.get_ticks()  # Update current time
    clock.tick(FPS)

    if speed == True:
        if current_time - last_time_speed > delay_speed:
            last_time_speed = current_time
            speed_foreign_vehicles += 0.1
            delay_center_line_road -= 0.1

    # Event loop to handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the window close button is pressed
            running = False  # Exit the game loop
    
    # Add new center line segments at a certain delay
    if current_time - last_time_center_line_road > delay_center_line_road:
        last_time_center_line_road = current_time
        center_line_road.append([400, -70])  # Start new line at the top of the road

    # Add new foreign vehicles segments at a certain delay
    if current_time - last_time_foreign_vehicles > delay_foreign_vehicles:
        last_time_foreign_vehicles = current_time
        foreign_vehicles_array.append([random.randint(200, 600), -70])  # Start new vehicle at a random x position
    
    screen.fill([0, 255, 0])  # Fill the screen ground with green color

    # Drawing the road
    width_road = 500  # Width of the road
    height_road = 600  # Height of the road (to cover the entire screen height)
    middle_road = screen_width / 2  # Center point of the screen width
    x_road = middle_road - (width_road / 2)  # Calculate the x position to center the road
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(x_road, 0, width_road, height_road))  # Draw the road

    # Update and draw each line in the center line road
    for line in center_line_road:
        line[1] += speed_center_line_road  # Move the line downward
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(line[0], line[1], 10, 60))  # Draw the line
        # Remove line if it moves out of the screen
        if line[1] > screen_height + 70:
            center_line_road.remove(line)

    # Update and draw each foreign vehicle in the foreign vehicles array
    for foreign_vehicle in foreign_vehicles_array:
        foreign_vehicle[1] += speed_foreign_vehicles  # Move the foreign vehicle downward
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(foreign_vehicle[0], foreign_vehicle[1], 30, 50))  # Draw the foreign vehicle
        # Remove vehicle if it moves out of the screen
        if foreign_vehicle[1] > screen_height + 70:
            foreign_vehicles_array.remove(foreign_vehicle)

    # Drawing the player car
    player_car.car(screen, (0, 0, 255), x_car_player - middle_car_player, y_car_player, width_car_player, height_car_player)  # Draw the player car

    # Player car movement
    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # If 'A' key or left arrow is pressed, move the car left
        x_car_player -= speed_car_player
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # If 'D' key or right arrow is pressed, move the car right
        x_car_player += speed_car_player        

    # Collision detection between player car and foreign vehicles
    player_rect = pygame.Rect(x_car_player - middle_car_player, y_car_player, width_car_player, height_car_player)
    for foreign_vehicle in foreign_vehicles_array:
        foreign_vehicle_rect = pygame.Rect(foreign_vehicle[0], foreign_vehicle[1], 30, 50)
        if player_rect.colliderect(foreign_vehicle_rect):  # If collision occurs
            running = False  # Stop the game

    pygame.display.flip()  # Update the screen with the latest changes

pygame.quit()  # Quit Pygame when the game loop ends
