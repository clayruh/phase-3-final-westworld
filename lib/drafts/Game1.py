import pygame

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

circle_radius = 40
player_pos = pygame.Vector2(screen_width / 2, screen_height / 2)


maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]



while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill("purple")

    # Draw the circle
    pygame.draw.circle(screen, "red", player_pos, circle_radius)

    keys = pygame.key.get_pressed()

    # Draw the walls
    

    # Calculate the new position based on user input and delta time
    speed = 300  # You can adjust this value to control the circle's speed
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt

    # Ensure the circle stays within the screen boundaries
    player_pos.x = max(circle_radius, min(player_pos.x, screen_width - circle_radius))
    player_pos.y = max(circle_radius, min(player_pos.y, screen_height - circle_radius))

    # flip() the display to put your work on the screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
