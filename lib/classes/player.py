import pygame

# -----------Player class----------- #
class Player(pygame.sprite.Sprite):
    def __init__(self, square_center, square_radius, square_rect, maze):
        super().__init__()
        original_icon = pygame.image.load("./assets/images/black-hat.png")
        scaled_width = original_icon.get_width() // 2
        scaled_height = original_icon.get_height() // 2
        self.image = pygame.transform.scale(original_icon, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.radius = 10

        self.position = pygame.Vector2(square_center.x - square_radius + 10, square_center.y)
        self.square_rect = square_rect
        self.maze = maze
        self.speed = 20

    def draw(self, screen):
        screen.blit(self.image, self.position - pygame.Vector2(self.radius, self.radius))

    def move(self, keys):
        move_vector = pygame.Vector2(0, 0)
        if keys[pygame.K_UP]:
            move_vector.y = -self.speed
        if keys[pygame.K_DOWN]:
            move_vector.y = self.speed
        if keys[pygame.K_LEFT]:
            move_vector.x = -self.speed
        if keys[pygame.K_RIGHT]:
            move_vector.x = self.speed

        new_position = self.position + move_vector

        # Check if the new position is within the square boundary and not in the walls
        new_rect = pygame.Rect(new_position.x - self.radius, new_position.y - self.radius, self.radius * 2, self.radius * 2)
        if self.square_rect.contains(new_rect) and not any(wall.colliderect(new_rect) for wall in self.maze):
            # Apply the new position if it's within the boundary
            self.position = new_position