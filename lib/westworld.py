import pygame
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

# ----------Maze attributes----------#
# Define the boundary of the maze as a circle
circle_radius = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2 - 20  # Adjust the radius as needed
circle_center = pygame.Vector2(circle_radius + 20, SCREEN_HEIGHT / 2)  # Shifted to the left

# Define the maze structure (1 represents walls, 0 represents open paths)
maze_radius = circle_radius  # Make the inner radius smaller to fit the page vertically
num_walls = 7200  # Adjust the number of walls as needed
angle_step = 2 * math.pi / num_walls
wall_thickness = 5  # Adjust the thickness of the circular boundary
wall_color = (0, 0, 0)  # Black

maze = []
for i in range(num_walls):
    start_angle = i * angle_step
    end_angle = (i + 1) * angle_step  # Make walls one full angle step long
    start_x = int(circle_center.x + maze_radius * math.cos(start_angle))
    start_y = int(circle_center.y + maze_radius * math.sin(start_angle))
    end_x = int(circle_center.x + maze_radius * math.cos(end_angle))
    end_y = int(circle_center.y + maze_radius * math.sin(end_angle))
    maze.append((start_x, start_y, end_x, end_y))

# -----------Player class----------- #
class Player(pygame.sprite.Sprite):
    def __init__(self):
        global circle_center # change when we make maze class
        global circle_radius # change when we make maze class
        super().__init__()
        self.image = pygame.image.load("./assets/images/cowboy-hat-small.png")
        self.rect = self.image.get_rect()
        self.rect.center = (circle_center.x - circle_radius + 10, circle_center.y)

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
        pygame.draw.line(screen, wall_color, wall[:2], wall[2:], wall_thickness)

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

    # Check if the new position is within the circular boundary and not in the walls
    if (
        (player.rect.center - circle_center).length() <= circle_radius - player.radius()
    ):
        player.rect = new_rect

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
