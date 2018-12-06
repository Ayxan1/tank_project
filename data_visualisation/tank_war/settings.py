class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 10
        self.bullet_height = 35
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
