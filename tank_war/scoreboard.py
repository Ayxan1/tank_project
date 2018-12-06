import pygame.font
class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, screen, enemy_tank, tank):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score(enemy_tank, tank)

    def prep_score(self, enemy_tank, tank):
        """Turn the score into a rendered image."""
        score_str = 'Enemy --- ' + str(enemy_tank.enemy_health) + '    ' + 'Player --- ' + str(tank.player_health)
        self.score_image = self.font.render(score_str, True, self.text_color, (201, 232, 77))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 100
        self.score_rect.top = 30

    def show_score(self):
         """Draw score to the screen."""
         self.screen.blit(self.score_image, self.score_rect)
