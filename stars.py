import pygame
import random
from pygame import *
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
pygame.init()
class Etoile(pygame.sprite.Sprite):
    def __init__(self):
        super(Etoile, self).__init__()
        self.surf = pygame.image.load("assets/star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                LARGEUR_ECRAN + 20,
                random.randint(0, HAUTEUR_ECRAN)
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

CREATE_STAR = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_STAR, 50)
the_stars = pygame.sprite.Group()