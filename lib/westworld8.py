import pygame
import math
import random

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

# Define the boundary of the maze as a circle
circle_radius = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2 - 20
circle_center = pygame.Vector2(circle_radius + 20, SCREEN_HEIGHT / 2)

# Define the maze structure (1 represents walls, 0 represents open paths)
maze_radius = circle_radius - 20  # Make the inner radius smaller for the maze
maze_width = 2 * circle_radius
maze_height = 2 * circle_radius
maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]

# Create the maze using a randomized depth-first search algorithm
stack = [((int(circle_center.x - circle_radius + 10), int(circle_center.y)))]
while stack:
    x, y = stack[-1]
    maze[y][x] = 0
    neighbors = [(x + dx, y + dy) for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]]
    unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < maze_width and 0 <= ny < maze_height and maze[ny][nx] == 1]
    if unvisited_neighbors:
        nx, ny = random.choice(unvisited_neighbors)
        stack.append((nx, ny))
    else:
        stack.pop()

# pygame setup
wall_thickness = 5
wall_color = (0, 0, 0)
player_color = (255, 0, 0)

player_radius = 10
player_pos = pygame.Vector2(int(circle_center.x - circle_radius + 10), int(circle_center.y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, wall_color, (x * wall_thickness, y * wall_thickness, wall_thickness, wall_thickness))

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

    if (
        (new_player_pos - circle_center).length() <= circle_radius - player_radius and
        maze[int(new_player_pos.y)][int(new_player_pos.x)] == 0
    ):
        player_pos = new_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
