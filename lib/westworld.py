import pygame
import math

<<<<<<< Updated upstream
# Initialize screen
=======
# ----------Initialize screen---------#
>>>>>>> Stashed changes
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background_image = pygame.image.load("../assets/images/westworld__the_maze_logo_by_mattwilliamsart_daqww0w-pre.jpeg")
background_image = pygame.image.load('./assets/images/valley.jpeg')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
# dt = 0
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
        super().__init__()
        self.image = pygame.image.load("../assets/images/cowboy-hat.svg")
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    player_color = (255, 0, 0)  # Red

    player_radius = 10  # Adjust the player circle size (smaller)
    player_pos = pygame.Vector2((circle_center.x - circle_radius + 10), circle_center.y)

player = Player()

# checking for image
player_icon = pygame.image.load('../assets/images/cowboy-hat.png')
imagerect = player_icon.get_rect()
# how to add this as a Player class directly?


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
    player.draw(screen, player_color, (int(player_pos.x), int(player_pos.y)), player_radius)

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
