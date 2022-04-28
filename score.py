import pygame

from pygame import *
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
pygame.font.init()
police_score = pygame.font.SysFont('Comix Sans MS', 30)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self._scorecount = 0
        self._setText()

    def _setText(self):
        self.surf = police_score.render(
            'Score : ' + str(self._scorecount), False, (255, 255, 255)
        )
        self.rect = self.surf.get_rect(
            center = (LARGEUR_ECRAN / 2, 15)
        )

    def update(self):
        self._setText()
    def incremente(self, valeur):
        self._scorecount = self._scorecount + valeur