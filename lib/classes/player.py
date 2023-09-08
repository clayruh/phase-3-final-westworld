import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, square_center, square_radius, square_rect, maze, collide_up=0, collide_down=0, collide_left=0, collide_right=0):
        super().__init__()
        original_icon = pygame.image.load("./assets/images/black-hat-1.png")
        scaled_width = original_icon.get_width() // 2
        scaled_height = original_icon.get_height() // 2
        self.image = pygame.transform.scale(original_icon, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.radius = 10

        self.position = pygame.Vector2(square_center.x - square_radius + 10, square_center.y)
        self.square_rect = square_rect
        self.maze = maze
        self.speed = 20

        self.collide_up = collide_up
        self.collide_down = collide_down
        self.collide_left = collide_left
        self.collide_right = collide_right

    def draw(self, screen):
        screen.blit(self.image, self.position - pygame.Vector2(self.radius, self.radius))

    def move(self, keys):
        # print(self.rect)
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


    def breakwall(self,keys):
        move_vector = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            move_vector.y = -self.speed
            self.collide_up = 1
        if keys[pygame.K_s]:
            move_vector.y = self.speed
            self.collide_down = 1
        if keys[pygame.K_a]:
            move_vector.x = -self.speed
            self.collide_left = 1
        if keys[pygame.K_d]:
            move_vector.x = self.speed
            self.collide_right = 1

        new_position = self.position + move_vector
        # self.position = new_position

        # Check if the new position is within the square boundary and not in the walls
        new_rect = pygame.Rect(new_position.x - self.radius, new_position.y - self.radius, self.radius * 2, self.radius * 2)
        
        # Check for collision with any wall
        collided_wall = None
        for wall in self.maze:
            if wall.colliderect(new_rect) and (self.collide_up == 1 or self.collide_down == 1 or self.collide_left == 1 or self.collide_right == 1):
                collided_wall = wall
                break

        # If a wall was collided with and it's within the boundary, remove the wall and apply the new position
        if collided_wall and self.square_rect.contains(new_rect):
            self.maze.remove(collided_wall)
            # FREEDOM = pygame.font.render("Humans fancy that there's something special about the way we perceive the world, and yet we live in loops as tight and as closed as the hosts do, seldom questioning our choices, content, for the most part, to be told what to do next.", True, self.text_color)
            # screen.blit(FREEDOM, (750, 300))
            self.position = new_position

        # If there is now wall, the player can move freely in the open world
        else:
            self.position = new_position


# Humans fancy that there's something special about the way we perceive the world, and yet we live in loops as tight and as closed as the hosts do, seldom questioning our choices, content, for the most part, to be told what to do next."


        # We had to update the rect in order to recognize it's moved position ANNOYINGG

