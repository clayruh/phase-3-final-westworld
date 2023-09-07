import pygame
import math

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
circle_center = pygame.Vector2(circle_radius + 20, SCREEN_HEIGHT / 2)  # Shifted to the left

# Define the maze structure (1 represents walls, 0 represents open paths)
maze_radius = circle_radius  # Make the inner radius smaller to fit the page vertically
num_walls = 7200  # Adjust the number of walls as needed
angle_step = 2 * math.pi / num_walls

maze = []
for i in range(num_walls):
    start_angle = i * angle_step
    end_angle = (i + 1) * angle_step
    start_x = int(circle_center.x + maze_radius * math.cos(start_angle))
    start_y = int(circle_center.y + maze_radius * math.sin(start_angle))
    end_x = int(circle_center.x + maze_radius * math.cos(end_angle))
    end_y = int(circle_center.y + maze_radius * math.sin(end_angle))
    maze.append((start_x, start_y, end_x, end_y))

# pygame setup
wall_thickness = 5
wall_color = (0, 0, 0)
player_color = (255, 0, 0)
player_radius = 10
player_pos = pygame.Vector2(circle_center.x - circle_radius + 10, circle_center.y)

# Define the interior walls of the maze
interior_walls = [
    (300, 200, 400, 200),
    (400, 200, 400, 300),
    (400, 300, 600, 300),
    (600, 300, 600, 400),
    (600, 400, 500, 400),
    (500, 400, 500, 600),
    (500, 600, 700, 600),
    (700, 600, 700, 500),
    (700, 500, 800, 500),
    (800, 500, 800, 300),
    (800, 300, 700, 300),
    (700, 300, 700, 200),
    (700, 200, 600, 200),
    (600, 200, 600, 100),
    (600, 100, 400, 100),
    (400, 100, 400, 200)
    (400, 100, 400, 200)
    (400, 100, 400, 200)
    (400, 100, 400, 200)
    
]

# Extend the maze list with interior walls
maze.extend(interior_walls)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
        move_vector = pygame.Vector2(0, -speed * dt)
    if keys[pygame.K_DOWN]:
        move_vector = pygame.Vector2(0, speed * dt)
    if keys[pygame.K_LEFT]:
        move_vector = pygame.Vector2(-speed * dt, 0)
    if keys[pygame.K_RIGHT]:
        move_vector = pygame.Vector2(speed * dt, 0)

    new_player_pos = player_pos + move_vector

    # Check if the new position is within the circular boundary and not in the walls
    if (
        (new_player_pos - circle_center).length() <= circle_radius - player_radius
    ):
        # Check if the new position is not colliding with walls
        collides_with_walls = False
        for wall in interior_walls:
            wall_rect = pygame.Rect(*wall)
            player_rect = pygame.Rect(new_player_pos.x - player_radius, new_player_pos.y - player_radius, player_radius * 2, player_radius * 2)
            if player_rect.colliderect(wall_rect):
                collides_with_walls = True
                break

        if not collides_with_walls:
            player_pos = new_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
