import pygame
from pygame.sprite import Sprite
import math
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_settings, screen, tank):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        """
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = tank.rect.centerx
        self.rect.centery = tank.rect.centery
        """
        self.bullet_image = pygame.image.load('images/bullet.png').convert_alpha()
        self.rect = self.bullet_image.get_rect()



        # Origin angle of fired bullet
        self.origin_angle = tank.angle
        self.temporary_angle = tank.angle

        # preventing extending range(-360, 360)
        if self.temporary_angle > 360 or self.temporary_angle < -360:
            if self.temporary_angle > 360:
                self.origin_angle = self.origin_angle - 360
            else:
                self.origin_angle = self.origin_angle + 360

        # Finding tang.
        self.bullet_difference_between_x_y =  -math.tan(self.origin_angle * math.pi / 180)



        # Rotating of bullet.
        self.bullet_image = pygame.transform.rotozoom(self.bullet_image, self.origin_angle, 1)
        self.rect = self.bullet_image.get_rect()
        self.rect.centerx = tank.rect.centerx
        self.rect.centery = tank.rect.centery

        # Speed of bullet.
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.

        # Bullet delayer for sharp angles.
        delayer_x = 1
        delayer_y = 0

        # Tang function has no value for 90 and 270 anngles for preventing error.
        if self.origin_angle == 270 or self.origin_angle == -270 or self.origin_angle == 90 or self.origin_angle == -90:
            if self.origin_angle == -90 or self.origin_angle == 270:
                self.rect.centerx += int((self.speed_factor))
            else:
                self.rect.centerx -= int((self.speed_factor))
        else:
            if (self.origin_angle < -70 and self.origin_angle > -110) or (self.origin_angle < 110 and self.origin_angle > 70):
                delayer_x = 0.3
                delayer_y = 7
            if (self.origin_angle < -90 and self.origin_angle > -270) or (self.origin_angle < 270 and self.origin_angle > 90):
                self.rect.centerx -= int((self.speed_factor * delayer_x) * (self.bullet_difference_between_x_y))
                self.rect.centery += int((self.speed_factor - 3 - delayer_y))
            else:
                self.rect.centerx += int((self.speed_factor * delayer_x) * (self.bullet_difference_between_x_y))
                self.rect.centery -= int((self.speed_factor - 3 - delayer_y))

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.bullet_image, self.rect)
