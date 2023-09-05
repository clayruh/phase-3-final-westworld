import pygame
# build everything in one file and then import the classes in

# Initialize screen
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("../assets/images/westworld__the_maze_logo_by_mattwilliamsart_daqww0w-pre.jpeg")
pygame.display.set_caption('Westworld')


# Initialize player position and attributes
player_radius = 20
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 100

# Game loop
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Calculate player movement
    dx = 0
    dy = 0

    if keys[pygame.K_UP]:
        dy = -player_speed * dt
    if keys[pygame.K_DOWN]:
        dy = player_speed * dt
    if keys[pygame.K_LEFT]:
        dx = -player_speed * dt
    if keys[pygame.K_RIGHT]:
        dx = player_speed * dt

    # Update player position
    player_x += dx
    player_y += dy

    # Ensure player stays within the window bounds
    player_x = max(player_radius, min(player_x, SCREEN_WIDTH - player_radius))
    player_y = max(player_radius, min(player_y, SCREEN_HEIGHT - player_radius))

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    # Draw the player circle
    pygame.draw.circle(screen, "red", (int(player_x), int(player_y)), player_radius)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()