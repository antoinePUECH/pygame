import pygame
import random
from pygame import *

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Ennemie(pygame.sprite.Sprite):
    def __init__(self):
        super(Ennemie, self).__init__()
        self.surf = pygame.image.load("assets/ennemi.webp").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (100, 50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                LARGEUR_ECRAN + 50,
                random.randint(0, HAUTEUR_ECRAN)
            )
        )
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()