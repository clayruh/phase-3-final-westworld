import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)

    def increment(self, amount):
        self.value += amount

    def show_score(self, screen):
        score_text = self.font.render("Score: " + str(self.value), True, self.text_color)
        screen.blit(score_text, (10, 10))