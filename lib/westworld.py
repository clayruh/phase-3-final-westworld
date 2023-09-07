import pygame
import random
from pygame import mixer
import sys
sys.path.append('./phase-3-final-westworld')
# from lib.classes.highscore import Highscore

from classes.player import Player

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
inner_wall_thickness = 10
wall_color = (0, 0, 0)

maze = [
    pygame.Rect(square_left, square_top, 20, square_size),
    pygame.Rect(square_left + square_size - 20, square_top, 20, square_size),
    pygame.Rect(square_left, square_top, square_size, 20),
    pygame.Rect(square_left, square_top + square_size - 20, square_size, 20)
]

# Randomly generate inner walls
num_inner_walls = 50  # Adjust the number of inner walls as needed
for _ in range(num_inner_walls):
    x = random.randint(square_left + 30, square_left + square_size - 30)
    y = random.randint(square_top + 30, square_top + square_size - 30)
    width = random.randint(20, 100)
    height = inner_wall_thickness
    maze.append(pygame.Rect(x, y, width, height))

# ------------------ Music ------------------- #
pygame.mixer.init()
pygame.mixer.music.load("./assets/sounds/westworld-theme.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# ---------------- Initialize game ----------------#

# Create instances
player = Player(square_center, square_radius, square_rect, maze)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the maze walls
    for wall in maze:
        pygame.draw.rect(screen, wall_color, wall)

    # Draw player onto screen
    player.draw(screen)

    # Handle player and movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
