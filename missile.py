import pygame

from pygame import *

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Missile(pygame.sprite.Sprite):
    def __init__(self, center_missile):
        super(Missile, self).__init__()
        self.surf = pygame.image.load("assets/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = center_missile
        )
    def update(self):
        self.rect.move_ip(25, 0)
        if self.rect.left > LARGEUR_ECRAN:
            self.kill()