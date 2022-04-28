import pygame, missile, ennemi, explosion, stars, score
from pygame import *
from ennemi import  Ennemie
from missile import Missile
from explosion import Explosion
from stars import *
from score import Score
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
all_sprite = pygame.sprite.Group()
the_missile = pygame.sprite.Group()
class Spatialship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spatialship, self).__init__()
        self.surf = pygame.image.load("assets/spacecraft.webp").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (75, 40))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
        if pressed_keys[K_SPACE]:
            if len(the_missile.sprites()) < 1:
                missile = Missile(self.rect.center)
                all_sprite.add(missile)
                the_missile.add(missile)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN
pygame.init()
pygame.display.set_caption("Save the earth")
CREATE_ENNEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENNEMY, 500)
screen = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])
clock = pygame.time.Clock()
the_ennemies = pygame.sprite.Group()
the_explosions = pygame.sprite.Group()
spacecraft = Spatialship()
all_sprite.add(spacecraft)
score = Score()
all_sprite.add(score)
play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == CREATE_ENNEMY:
            new_ennemi = Ennemie()
            the_ennemies.add(new_ennemi)
            all_sprite.add(new_ennemi)
        elif event.type == CREATE_STAR:
            new_star = Etoile()
            the_stars.add(new_star)
            all_sprite.add(new_star)

    screen.fill((0, 0, 0))
    if pygame.sprite.spritecollideany(spacecraft, the_ennemies):
        spacecraft.kill()
        explosion = Explosion(spacecraft.rect.center)
        the_explosions.add(explosion)
        all_sprite.add(explosion)
        play = False
    for missile in the_missile:
        ennemies_killed = pygame.sprite.spritecollide(missile, the_ennemies, True)
        if len(ennemies_killed) > 0:
            missile.kill()
            score.incremente(len(ennemies_killed))
        for ennemi in ennemies_killed:
            explosion = Explosion(ennemi.rect.center)
            the_explosions.add(explosion)
            all_sprite.add(explosion)
    pressed_key = pygame.key.get_pressed()
    spacecraft.update(pressed_key)
    the_missile.update()
    the_ennemies.update()
    the_explosions.update()
    the_stars.update()
    score.update()
    for my_sprite in all_sprite:
        screen.blit(my_sprite.surf, my_sprite.rect)
    screen.blit(spacecraft.surf, spacecraft.rect)
    pygame.display.flip()
    clock.tick(30)
pygame.time.delay(2000)
pygame.quit()