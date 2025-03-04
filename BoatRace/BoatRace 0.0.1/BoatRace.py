import pygame, random
pygame.init()

# Display setup
display = pygame.display.set_mode([1000, 700])
pygame.display.set_caption("BoatRace")

# FPS setup
FPS = 120
clock = pygame.time.Clock()

# Pause setup
paused = False

# Sound setup
shoot_laser_boat = pygame.mixer.Sound("bin/sfx/shoot/shoot_boat_race.wav")
fill_up = pygame.mixer.Sound("bin/sfx/fill_up/filling_up.wav")
explode = pygame.mixer.Sound("bin/sfx/crash/explosion_retro.wav")
moveSFX = pygame.mixer.Sound("bin/sfx/moving/move_boat.wav")
# slowSFX = pygame.mixer.Sound("sfx/crash/explosion_retro.wav")

# Player setup
x_player = 500
y_player = 600
player_width, player_height = 20, 40
speed_player = 2.5
def player(x, y):
    pygame.draw.rect(display, (0, 0, 255), (x, y, player_width, player_height))
    pygame.draw.rect(display, (0, 100, 0), (x+5, y+10, player_width-10, player_height-5))
    pygame.draw.rect(display, (100, 100, 100), (x+5, y+5, player_width-10, player_height-5))
    pygame.draw.rect(display, (0, 0, 255), (x+5, y-5, player_width-10, player_height-25))
    pygame.draw.rect(display, (255, 255, 255), (x+5, y+5, player_width-10, player_height-35))

# Enemy setup
enemy_array = []
enemy_width, enemy_height = 20, 40
last_spawn_enemy_time = 0
delay_spawn_enemy_time = 550
speed_enemy = 3
def enemy(x, y):
    pygame.draw.rect(display, (255, 0, 0), (x, y, enemy_width, enemy_height))
    pygame.draw.rect(display, (0, 100, 0), (x+5, y+10, player_width-10, player_height-5))
    pygame.draw.rect(display, (100, 100, 100), (x+5, y+5, player_width-10, player_height-5))
    pygame.draw.rect(display, (255, 0, 0), (x+5, y-5, player_width-10, player_height-25))
    pygame.draw.rect(display, (255, 255, 255), (x+5, y+5, player_width-10, player_height-35))

tree_array = []
tree_width, tree_height = 10, 10
last_spawn_tree_time = 0
delay_spawn_tree_time = 35
speed_tree = 5
def tree(x, y):
    # Drawing the leafs
    # pygame.draw.rect(display, (20, 100, 0), (x, y-10, tree_width, tree_height))
    pygame.draw.rect(display, (20, 100, 0), (x, y, tree_width, tree_height))
    pygame.draw.rect(display, (20, 100, 0), (x, y+10, tree_width, tree_height))
    # Drawing the right leafs
    pygame.draw.rect(display, (20, 100, 0), (x+10, y+10, tree_width, tree_height))
    # pygame.draw.rect(display, (20, 100, 0), (x+20, y+10, tree_width, tree_height))
    # Drawing the left leafs
    pygame.draw.rect(display, (20, 100, 0), (x-10, y+10, tree_width, tree_height))
    # pygame.draw.rect(display, (20, 100, 0), (x-20, y+10, tree_width, tree_height))
    # Drawing the woods
    pygame.draw.rect(display, (100, 50, 0), (x, y+20, tree_width, tree_height))
    # pygame.draw.rect(display, (100, 50, 0), (x, y+30, tree_width, tree_height))

fuel_array = []
x_fuel, y_fuel = 400, 350
fuel_width, fuel_height = 30, 60
last_spawn_fuel_time = 0
delay_spawn_fuel_time = random.choice([3000, 4000, 5000])
speed_fuel = 3
def fuel(x, y):
    pygame.draw.rect(display, (255, 60, 60), (x, y, fuel_width, fuel_height))
    pygame.draw.rect(display, (255, 255, 255), (x, y+15, 30, 15))
    pygame.draw.rect(display, (255, 255, 255), (x, y+45, 30, 15))

fuel_bar_width, fuel_bar_height = 300, 25
last_length_fuel_bar = 0
delay_decrease_length_fuel_bar = 100
delay_increase_length_fuel_bar = 100
def fuel_bar(x, y):
    pygame.draw.rect(display, (255, 150, 0), (x, y, fuel_bar_width, fuel_bar_height))

laser_width, laser_height = 10, 30
x_laser, y_laser = x_player, y_player
speed_laser = 17
shoot = False
def laser(x, y):
    pygame.draw.rect(display, (255, 255, 0), (x, y-1, laser_width, laser_height))
 
running = True
while running:       

    clock.tick(FPS)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Deteksi jika tombol ESC ditekan
                paused = not paused  # Ubah status jeda

    if paused:
        continue

    display.fill([0, 255, 255])

    if current_time - last_length_fuel_bar > delay_decrease_length_fuel_bar:
        last_length_fuel_bar = current_time
        fuel_bar_width -= 1
        if fuel_bar_width <= 0:
            running = False
    
    # Spawning Enemies
    if current_time - last_spawn_enemy_time > delay_spawn_enemy_time:
        last_spawn_enemy_time = current_time
        enemy_array.append([random.choice([250, 400, 550]), -100, random.uniform(-3,3)])
        # [0, 1, 2]
        # random.randint(120, 880)

    # Spawning Trees
    if current_time - last_spawn_tree_time > delay_spawn_tree_time:
        last_spawn_tree_time = current_time
        tree_array.append([random.choice([30, 50, 70, 930, 950, 970]), -20])

    # Spawning fuel
    if current_time - last_spawn_fuel_time > delay_spawn_fuel_time:
        last_spawn_fuel_time = current_time
        fuel_array.append([random.randint(150, 750), -100])

    # Player movement
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        speed_enemy = 4.5
        speed_tree = 6.5
        speed_fuel = 4.5
        fuel_bar_width -= 0.2
    elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        speed_enemy = 1.5
        speed_tree = 3.5
        speed_fuel = 1.5
        delay_decrease_length_fuel_bar = 150
    else:
        speed_enemy = 3
        speed_tree = 5
        speed_fuel = 3
        delay_decrease_length_fuel_bar = 100
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        x_player -= speed_player
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        x_player += speed_player
    if key_pressed[pygame.K_SPACE] and not shoot:
        shoot = True
        x_laser = x_player + player_width // 2 - laser_width // 2  # Posisikan peluru di tengah pemain
        y_laser = y_player
        shoot_laser_boat.play()
    if shoot == True:
        y_laser -= speed_laser
        laser(x_laser, y_laser)
        if y_laser <= -50:
            shoot = False
    # if not shoot:
    #     laser_rect = pygame.Rect(0, 0, 0, 0) 

   # ========== Drawing ==========

   # Drawing the healt bar
   

    # Drawing the ground
    left_ground = pygame.draw.rect(display, (0, 255, 0), pygame.Rect(0, 0, 100, 700))
    right_ground = pygame.draw.rect(display, (0, 255, 0), pygame.Rect(900, 0, 100, 700))

    player_rect = pygame.Rect(x_player, y_player, player_width, player_height) # the rect collider
    laser_rect = pygame.Rect(x_laser, y_laser, laser_width, laser_height)

    
    for fuels in fuel_array:
        fuels[1] += speed_fuel
        fuel(fuels[0], fuels[1])
        fuel_rect = pygame.Rect(fuels[0], fuels[1], fuel_width, fuel_height)
        if fuels[1] >= 750:
            fuel_array.remove(fuels)
        if player_rect.colliderect(fuel_rect):
            if current_time - last_length_fuel_bar > delay_increase_length_fuel_bar:
                last_length_fuel_bar = current_time
                fuel_bar_width += 15
                fill_up.play()
            if fuel_bar_width >= 300:
                fuel_bar_width = 300
        if fuel_rect.colliderect(laser_rect):
                fuel_array.remove(fuels)
                explode.play()
                shoot = False
                y_laser = y_player

    # Drawing the player
    player(x_player, y_player)

    # Drawing the enemy
    for enemies in enemy_array:
        enemies[1] += speed_enemy
        enemies[0] += enemies[2] # x_enemy that move randomly
         # Enemy Rect
        enemy(enemies[0], enemies[1])
        enemy_rect = pygame.Rect(enemies[0], enemies[1], enemy_width, enemy_height)
        # if the enemy colliderrect with left_ground or  right_ground then times by -1 and btw you also can code like this "if enemies[0] <= 120 or enemies[0] >= 880:"
        if enemy_rect.colliderect(left_ground) or enemy_rect.colliderect(right_ground):
            enemies[2] *= -1
        if enemies[1] >= 750: # if the enemy reach y = 750 then remove so your computer will not explode lol
            enemy_array.remove(enemies)
        if player_rect.colliderect(enemy_rect) or player_rect.colliderect(left_ground) or player_rect.colliderect(right_ground):
            running = False
        if enemy_rect.colliderect(laser_rect):
                enemy_array.remove(enemies)
                explode.play()
                shoot = False
                y_laser = y_player
    
    for trees in tree_array:
        trees[1] += speed_tree
        tree(trees[0], trees[1])
        if trees[1] >= 750:
            tree_array.remove(trees)

    fuel_bar(30, 660)

    pygame.display.flip()

pygame.quit()
