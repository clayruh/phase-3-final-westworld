import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_ball = pygame.image.load("./assets/images/red-ball.png")
        scaled_width = original_ball.get_width() // 7
        scaled_height = original_ball.get_height() // 7
        self.image = pygame.transform.scale(original_ball, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass