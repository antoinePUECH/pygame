import pygame

from pygame import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center_vaisseau):
        super(Explosion, self).__init__()
        self._compteur = 10
        self.surf = pygame.image.load("assets/explosion.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = center_vaisseau
        )

    def update(self):
        self._compteur = self._compteur - 1
        if self._compteur == 0:
            self.kill()