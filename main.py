import pygame
import spacecraft
from pygame import *
from spacecraft import Vaisseau

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

pygame.init()
pygame.display.set_caption("Save the earth")
ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])
clock = pygame.time.Clock()
vaisseau = Vaisseau()
continuer = True
while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    ecran.fill((0, 0, 0))
    touche_appuyee = pygame.key.get_pressed()
    vaisseau.update(touche_appuyee)
    ecran.blit(vaisseau.surf, vaisseau.rect)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()