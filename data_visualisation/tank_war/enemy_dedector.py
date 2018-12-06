import pygame
import math
import sys
class EnemyDedector():

    def __init__(self, screen, enemy_tank):
        # Enemy tank dedector
        self.screen = screen
        self.dedector_image = pygame.image.load('images/full_dedector.png').convert_alpha()
        self.rect = self.dedector_image.get_rect()
        self.rect.centerx = enemy_tank.rect.centerx
        self.rect.centery = enemy_tank.rect.centery
        self.dedector_angle = 0

    def rotate_dedector(self, enemy_tank):
        if self.dedector_angle > 360:
            self.dedector_angle = self.dedector_angle - 360
        elif self.dedector_angle < -360:
            self.dedector_angle = self.dedector_angle + 360
        self.dedector_angle += 3
        self.rect.centerx = enemy_tank.rect.centerx
        self.rect.centery = enemy_tank.rect.centery
        image = pygame.transform.rotozoom(self.dedector_image, self.dedector_angle, 1)
        dedector_rect = image.get_rect()
        dedector_rect.centerx = enemy_tank.rect.centerx
        dedector_rect.centery = enemy_tank.rect.centery
        self.rect = dedector_rect
        self.screen.blit(image, self.rect)
