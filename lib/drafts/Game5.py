import pygame
import math

# Set up the Pygame window
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

# Define the circular boundary
circle_radius = min(screen_width, screen_height) // 2 - 20  # Adjust the radius as needed
circle_center = pygame.Vector2(circle_radius + 20, screen_height / 2)  # Shifted to the left

# Define the maze structure (1 represents walls, 0 represents open paths)
maze_radius = circle_radius - 10  # Make the inner radius smaller to fit the page vertically
num_walls = 360  # Adjust the number of walls as needed
angle_step = 2 * math.pi / num_walls

maze = []
for i in range(num_walls):
    start_angle = i * angle_step
    end_angle = (i + 1) * angle_step  # Make walls one full angle step long
    start_x = int(circle_center.x + maze_radius * math.cos(start_angle))
    start_y = int(circle_center.y + maze_radius * math.sin(start_angle))
    end_x = int(circle_center.x + maze_radius * math.cos(end_angle))
    end_y = int(circle_center.y + maze_radius * math.sin(end_angle))
    maze.append((start_x, start_y, end_x, end_y))

# pygame setup
wall_thickness = 10  # Adjust the thickness of the circular boundary
wall_color = (0, 0, 0)  # Black
player_color = (255, 0, 0)  # Red

player_radius = 10  # Adjust the player circle size (smaller)
player_pos = pygame.Vector2(circle_center.x, circle_center.y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

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
        (new_player_pos - circle_center).length() <= circle_radius - player_radius
    ):
        # Apply the new position if it's within the boundary
        player_pos = new_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
