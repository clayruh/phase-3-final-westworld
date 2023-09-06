import pygame
import math
# build everything in one file and then import the classes in

# Initialize screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background_image = pygame.image.load("../assets/images/westworld__the_maze_logo_by_mattwilliamsart_daqww0w-pre.jpeg")
background_image = pygame.image.load('./assets/images/valley.jpeg')  # 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption('Westworld')

# Define the boundary of the maze as a square
square_radius = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2 - 20  # Adjust the radius as needed
square_center = pygame.Vector2(square_radius + 20, SCREEN_HEIGHT / 2)  # Shifted to the left

# Define the maze structure (1 represents walls, 0 represents open paths)
maze_radius = square_radius  # Make the inner radius smaller to fit the page vertically
num_walls = 4  # Adjust the number of walls as needed
angle_step = 90


maze = []
for i in range(num_walls):
    start_angle = i * angle_step
    end_angle = (i + 1) * angle_step  # Make walls one full angle step long
    start_x = int(square_center.x + maze_radius)
    start_y = int(square_center.y + maze_radius)
    end_x = int(square_center.x + maze_radius )
    end_y = int(square_center.y + maze_radius)
    maze.append((start_x, start_y, end_x, end_y))

# pygame setup
wall_thickness = 5  # Adjust the thickness of the circular boundary
wall_color = (0, 0, 0)  # Black
player_color = (255, 0, 0)  # Red

player_radius = 10  # Adjust the player circle size (smaller)
player_pos = pygame.Vector2((square_center.x - square_radius + 10), square_center.y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the maze walls
    for wall in maze:
        pygame.draw.line(screen, wall_color, wall[:2], wall[2:], wall_thickness)

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

    # Check if the new position is within the circular boundary and not in the walls
    if (
        (new_player_pos - square_center).length() <= square_radius - player_radius
    ):
        # Apply the new position if it's within the boundary
        player_pos = new_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
