import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/images/red-ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.visible = True
        # print(self.rect)

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

    def update(self):
        pass

    def hide(self):
        self.visible = False