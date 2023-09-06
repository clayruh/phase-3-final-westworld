import pygame
import random
import math
from classes.highscore import Highscore


# ----------Initialize screen---------#
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

pygame.init()
background_image = pygame.image.load('./assets/images/valley.jpeg')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Westworld')


# Define the boundary of the maze as a square on the left side of the screen
square_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) - 40  # Adjust the size as needed
square_left = 20  # Adjust the left position as needed
square_top = (SCREEN_HEIGHT - square_size) // 2
square_rect = pygame.Rect(square_left, square_top, square_size, square_size)
square_radius = square_size/2
square_center_x = square_left + square_radius
square_center_y = square_top + square_radius
square_center = pygame.Vector2(square_center_x, square_center_y)


# Define the maze structure (1 represents walls, 0 represents open paths)
maze = [
    pygame.Rect(square_left, square_top, 20, square_size),
    pygame.Rect(square_left + square_size - 20, square_top, 20, square_size),
    pygame.Rect(square_left, square_top, square_size, 20),
    pygame.Rect(square_left, square_top + square_size - 20, square_size, 20)
]

# Generate inner walls to create paths
inner_wall_thickness = 10
inner_wall_color = (0, 0, 0)

# Randomly generate inner walls
num_inner_walls = 50  # Adjust the number of inner walls as needed
for _ in range(num_inner_walls):
    x = random.randint(square_left + 30, square_left + square_size - 30)
    y = random.randint(square_top + 30, square_top + square_size - 30)
    width = random.randint(20, 100)
    height = inner_wall_thickness
    maze.append(pygame.Rect(x, y, width, height))

# pygame setup
wall_thickness = 5
wall_color = (0, 0, 0)
# player_pos = pygame.Vector2(square_left + 30, square_top + 30)



# -----------Player class----------- #
class Player(pygame.sprite.Sprite):
    def __init__(self):
        global square_center # change when we make maze class
        global square_radius # change when we make maze class
        super().__init__()
        self.image = pygame.image.load("./assets/images/cowboy-hat-small.png")
        self.rect = self.image.get_rect()
        self.rect.center = (square_center.x - square_radius + 10, square_center.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def radius(self):
        return 10

player = Player()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the maze walls
    for wall in maze:
        pygame.draw.rect(screen, wall_color, wall)

    player.draw(screen)

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

    new_rect = player.rect.move(move_vector)

    # Check if the new position is within the square boundary and not in the walls
    if square_rect.collidepoint(new_player_pos) and not any(wall.colliderect(pygame.Rect(new_player_pos.x - player.radius(), new_player_pos.y - player.radius(), player.radius() * 2, player.radius() * 2)) for wall in maze):
        # Apply the new position if it's within the boundary
        player_pos = new_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
