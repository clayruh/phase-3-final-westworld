import pygame
import random
from pygame import mixer
import sys
sys.path.append('./phase-3-final-westworld/lib')

from classes.player import Player
from classes.ball import Ball
from classes.score import Score
from classes.highscore import Highscore

# ----------Initialize screen--------- # 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

pygame.init()
background_image = pygame.image.load('./assets/images/Westworld-background.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Westworld')

# ---------------- Maze ---------------- # 
# Define the boundary of the maze as a square on the left side of the screen
square_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) - 40  # Adjust the size as needed
square_left = 20
square_top = (SCREEN_HEIGHT - square_size) // 2
square_rect = pygame.Rect(square_left, square_top, square_size, square_size)
square_radius = square_size/2
square_center_x = square_left + square_radius
square_center_y = square_top + square_radius
square_center = pygame.Vector2(square_center_x, square_center_y)

# Generate inner walls to create paths
wall_thickness = 10
wall_color = (0, 0, 0)

maze = [
    pygame.Rect(square_left, square_top, 20, square_size),
    pygame.Rect(square_left + square_size - 20, square_top, 20, square_size),
    pygame.Rect(square_left, square_top, square_size, 20),
    pygame.Rect(square_left, square_top + square_size - 20, square_size, 20)
]

# Create a grid for the maze generation
cell_size = 80
num_cells_x = (square_size - 2 * wall_thickness) // cell_size  # Adjust for the inner walls
num_cells_y = (square_size - 2 * wall_thickness) // cell_size  # Adjust for the inner walls

grid = [['wall' for _ in range(num_cells_x)] for _ in range(num_cells_y)]

# Define the directions for moving to neighboring cells
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize starting cell
start_x = 0  # Set the starting X-coordinate to the leftmost cell
start_y = num_cells_y // 2  # Set the starting Y-coordinate to be roughly midway vertically

grid[start_y][start_x] = 'empty'

def carve(x, y):
    grid[y][x] = 'empty'
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + 1 * dx, y + 1 * dy
        if 0 <= nx < num_cells_x and 0 <= ny < num_cells_y and grid[ny][nx] == 'wall':
            # Calculate maze positions based on square_rect
            maze_x = square_rect.left + wall_thickness + (nx * cell_size)
            maze_y = square_rect.top + wall_thickness + (ny * cell_size)
            maze_width = wall_thickness if dx == 0 else cell_size
            maze_height = wall_thickness if dy == 0 else cell_size
            maze_rect = pygame.Rect(maze_x, maze_y, maze_width, maze_height)
            maze.append(maze_rect)
            carve(nx, ny)

carve(start_x, start_y)

# ------------------ Music ------------------- #
pygame.mixer.init()
pygame.mixer.music.load("./assets/sounds/westworld-theme.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# ---------------- Initialize game ----------------#
ball_positions = []
ball_radius = 10
ball = Ball(SCREEN_WIDTH //2, SCREEN_HEIGHT //2)

# Function to check if a position is valid for placing a ball
def is_valid_ball_position(position, maze):
    # Check if the position is within the maze and not colliding with walls
    for wall in maze:
        if wall.colliderect(position):
            return False
    return True

# Generate balls in the maze ------------------------#
while len(ball_positions) < 10:
    x = random.randint(square_left + wall_thickness, square_left + square_size - wall_thickness)
    y = random.randint(square_top + wall_thickness, square_top + square_size - wall_thickness)
    position = pygame.Rect(x, y, ball_radius * 2, ball_radius * 2)
    if is_valid_ball_position(position, maze):
        ball_positions.append(position)

balls = [Ball(position.centerx, position.centery) for position in ball_positions]

player = Player(square_center, square_radius, square_rect, maze)
score = Score()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(balls)

ball_group = pygame.sprite.Group()
ball_group.add(balls)

player_group = pygame.sprite.Group()
player_group.add()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the maze walls
    for wall in maze:
        pygame.draw.rect(screen, wall_color, wall)

    collisions = pygame.sprite.spritecollide(player, balls, False)
    # print(collisions)
    for ball in collisions: 
        if ball.visible == True:
            score.increment(10)
            ball.hide()

    # Draw balls onto screen
    for ball in balls:
        ball.draw(screen)

    # Display score
    score.show_score(screen)

    # Draw player onto screen
    player.draw(screen)
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.breakwall(keys)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
