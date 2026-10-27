import pygame

# Initialize Pygame
pygame.init()

# Window setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Box & Moving Obstacle")
clock = pygame.time.Clock()

# Player properties
player_x = 400
player_y = 300
player_size = 50
player_speed = 5

# Obstacle properties & Speed
obstacle_rect = pygame.Rect(200, 150, 80, 80)
obstacle_speed = 4  # How fast and which direction it moves

running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Game Logic
    
    # --- Player Movement ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Screen boundaries for player
    if player_x < 0: player_x = 0
    elif player_x > 800 - player_size: player_x = 800 - player_size
    if player_y < 0: player_y = 0
    elif player_y > 600 - player_size: player_y = 600 - player_size

    # --- Obstacle Automatic Movement ---
    obstacle_rect.x += obstacle_speed  # Move the red box every frame

    # Bounce off the left and right walls of the screen
    if obstacle_rect.left <= 0 or obstacle_rect.right >= 800:
        obstacle_speed *= -1  # Flip direction!

    # --- Collision Detection ---
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    if player_rect.colliderect(obstacle_rect):
        player_color = (255, 0, 0)  # Turns red if touching
    else:
        player_color = (0, 200, 255) # Blue otherwise

    # 3. Drawing / Rendering
    screen.fill((30, 30, 30))  # Clear screen

    # Draw obstacle and player
    pygame.draw.rect(screen, (200, 50, 50), obstacle_rect)
    pygame.draw.rect(screen, player_color, player_rect)

    # Refresh display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()