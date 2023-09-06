import pygame

# Initialize screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

pygame.init()
background_image = pygame.image.load('./assets/images/valley.jpeg')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption('Westworld')

# Define the boundary of the maze as a square on the left side of the screen
square_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) - 40  # Adjust the size as needed
square_left = 20  # Adjust the left position as needed
square_top = (SCREEN_HEIGHT - square_size) // 2
square_rect = pygame.Rect(square_left, square_top, square_size, square_size)

# Define the maze structure (1 represents walls, 0 represents open paths)
maze = [
    pygame.Rect(square_left, square_top, 20, square_size),
    pygame.Rect(square_left + square_size - 20, square_top, 20, square_size),
    pygame.Rect(square_left, square_top, square_size, 20),
    pygame.Rect(square_left, square_top + square_size - 20, square_size, 20)
]

# pygame setup
wall_thickness = 5
wall_color = (0, 0, 0)
player_color = (255, 0, 0)

player_radius = 10
player_pos = pygame.Vector2(square_left + 30, square_top + 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the maze walls
    for wall in maze:
        pygame.draw.rect(screen, wall_color, wall)

    # Draw the smaller player circle
    pygame.draw.circle(screen, player_color, (int(player_pos.x), int(player_pos.y)), player_radius)

    keys = pygame.key.get_pressed()
    speed = 150

    move_vector = pygame.Vector2(0, 0)
    if keys[pygame.K_UP]:
        move_vector.y = -speed * dt
    if keys[pygame.K_DOWN]:
        move_vector.y = speed * dt
    if keys[pygame.K_LEFT]:
        move_vector.x = -speed * dt
    if keys[pygame.K_RIGHT]:
        move_vector.x = speed * dt

    new_player_pos = player_pos + move_vector

    # Check if the new position is within the square boundary and not in the walls
    if square_rect.collidepoint(new_player_pos) and not any(wall.colliderect(pygame.Rect(new_player_pos.x - player_radius, new_player_pos.y - player_radius, player_radius * 2, player_radius * 2)) for wall in maze):
        # Apply the new position if it's within the boundary
        player_pos = new_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
