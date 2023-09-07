import pygame
import random
import math
import sys
sys.path.append('./phase-3-final-westworld')
# from lib.classes.highscore import Highscore

from classes.player import Player

# ----------Initialize screen--------- # 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

pygame.init()
background_image = pygame.image.load('./assets/images/valley.jpeg')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Westworld')

# Maze setup
maze = []
wall_color = (0, 0, 0)
wall_thickness = 10

# Create the outer boundaries of the maze as a square
square_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) - 2 * wall_thickness
square_rect = pygame.Rect(wall_thickness, wall_thickness, square_size, square_size)
maze.append(square_rect)

# Create a grid for the maze generation
cell_size = 40
num_cells_x = (square_size - wall_thickness) // cell_size
num_cells_y = (square_size - wall_thickness) // cell_size

grid = [['wall' for _ in range(num_cells_x)] for _ in range(num_cells_y)]

# Define the directions for moving to neighboring cells
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize starting cell
start_x = random.randint(0, num_cells_x - 1)
start_y = random.randint(0, num_cells_y - 1)
grid[start_y][start_x] = 'empty'

def carve(x, y):
    grid[y][x] = 'empty'
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < num_cells_x and 0 <= ny < num_cells_y and grid[ny][nx] == 'wall':
            maze_x = wall_thickness + nx * cell_size
            maze_y = wall_thickness + ny * cell_size
            maze_width = wall_thickness if dx == 0 else cell_size
            maze_height = wall_thickness if dy == 0 else cell_size
            maze_rect = pygame.Rect(maze_x, maze_y, maze_width, maze_height)
            maze.append(maze_rect)
            carve(nx, ny)

carve(start_x, start_y)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the maze walls
    for wall in maze:
        pygame.draw.rect(screen, wall_color, wall)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()