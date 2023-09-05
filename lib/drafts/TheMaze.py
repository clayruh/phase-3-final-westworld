import pygame
import math

# Pygame setup
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# Define maze parameters
maze_radius = 300  # Adjust the maze size
wall_thickness = 20  # Adjust the wall thickness
wall_color = (0, 0, 0)  # Black

# Define the center of the maze
maze_center = (screen_width // 2, screen_height // 2)

# Create a list of wall segments (lines) for the outer circle
num_segments = 36  # Adjust the number of segments
angle_step = 2 * math.pi / num_segments

maze_walls_outer = []
for i in range(num_segments):
    start_angle = i * angle_step
    end_angle = (i + 1) * angle_step
    start_x = int(maze_center[0] + maze_radius * math.cos(start_angle))
    start_y = int(maze_center[1] + maze_radius * math.sin(start_angle))
    end_x = int(maze_center[0] + maze_radius * math.cos(end_angle))
    end_y = int(maze_center[1] + maze_radius * math.sin(end_angle))
    maze_walls_outer.append(((start_x, start_y), (end_x, end_y)))

# Create a list of wall segments for the inner circle (interior maze)
inner_maze_radius = maze_radius * 0.6  # Adjust the inner maze size
maze_walls_inner = []

# Define the number of walls in the inner maze
num_inner_walls = 12  # Adjust the number of walls
inner_angle_step = 2 * math.pi / num_inner_walls

for i in range(num_inner_walls):
    start_angle = i * inner_angle_step
    end_angle = (i + 0.5) * inner_angle_step  # Make walls slightly shorter
    start_x = int(maze_center[0] + inner_maze_radius * math.cos(start_angle))
    start_y = int(maze_center[1] + inner_maze_radius * math.sin(start_angle))
    end_x = int(maze_center[0] + inner_maze_radius * math.cos(end_angle))
    end_y = int(maze_center[1] + inner_maze_radius * math.sin(end_angle))
    maze_walls_inner.append(((start_x, start_y), (end_x, end_y)))

# Pygame main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # White background

    # Draw the maze walls (outer circle)
    for wall in maze_walls_outer:
        pygame.draw.line(screen, wall_color, wall[0], wall[1], wall_thickness)

    # Draw the maze walls (inner circle)
    for wall in maze_walls_inner:
        pygame.draw.line(screen, wall_color, wall[0], wall[1], wall_thickness)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
