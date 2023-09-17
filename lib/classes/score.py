import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
        self.text_color = (99, 46, 33)
        #initiate high score
        self.highscore = 0


    def increment(self, amount):
        self.value += amount

    def show_score(self, screen):
        score_text = self.font.render("Score: " + str(self.value), True, self.text_color)
        screen.blit(score_text, (750, 20))
        
    def display(self, screen, SCREEN_WIDTH):
        font = pygame.font.Font('freesansbold.ttf', 32)

        # Display Score
        score_text = font.render(f'Score: {self.value}', True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topright = (SCREEN_WIDTH - 20, 20)  # 20 pixels from the right, 20 pixels from the top
        screen.blit(score_text, score_rect)

        # Display High Score
        highscore_text = font.render(f'High Score: {self.highscore}', True, (255, 255, 255))
        highscore_rect = highscore_text.get_rect()
        highscore_rect.topright = (SCREEN_WIDTH - 20, 60)  # 20 pixels from the right, 60 pixels from the top
        screen.blit(highscore_text, highscore_rect)
