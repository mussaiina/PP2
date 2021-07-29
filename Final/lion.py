import pygame
import random
import math
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1)
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Medina's Hungry Lion")
font = pygame.font.SysFont('times-new-roman', 20)
clock = pygame.time.Clock()
cnt_g = 0
cnt_r = 0
SCORE = 0
FONT = pygame.font.SysFont('verdana', 20)

is_going = True

WHITE = (255, 255, 255)
RED = (165, 6, 5)
BLUE = (37, 78, 138)
BLACK = (0, 0, 0)
GREEN = (0, 210, 57)
ORANGE = (255, 127, 39)
PI = math.pi


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.rect = self.surf.get_rect(center=(random.randint(25, 775), random.randint(25, 575)))
        self.image = pygame.image.load('icons/blue.png')
        self.color = BLUE

    def draw(self, x, y):
        pygame.draw.rect(screen, self.color, (x, y, 25, 25))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.centerx > 12.5:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_d] and self.rect.centerx < 787.5:
            self.rect.move_ip(5, 0)
        if keys[pygame.K_w] and self.rect.centery > 12.5:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_s] and self.rect.centery < 587.5:
            self.rect.move_ip(0, 5)


class Red(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.rect = self.surf.get_rect(center=(random.randint(25, 775), 0))
        self.image = pygame.image.load('icons/red.png')
        self.speed = random.randint(3, 7)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > height:
            self.rect = self.surf.get_rect(center=(random.randint(25, 775), 0))


class Green(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.rect = self.surf.get_rect(center=(random.randint(25, 775), 575))
        self.image = pygame.image.load('icons/green.png')
        self.speed = random.randint(3, 7)

    def move(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 0:
            self.rect = self.surf.get_rect(center=(random.randint(25, 775), 575))


P1 = Player()
R0 = Red()
R1 = Red()
R2 = Red()
R3 = Red()
R4 = Red()
R5 = Red()
R6 = Red()
R7 = Red()
R8 = Red()
R9 = Red()
G1 = Green()
G2 = Green()
G3 = Green()
G4 = Green()
G5 = Green()

entities = pygame.sprite.Group()
reds = pygame.sprite.Group()
greens = pygame.sprite.Group()

greens.add(G1)
greens.add(G2)
greens.add(G3)
greens.add(G4)
greens.add(G5)

reds.add(R0)
reds.add(R1)
reds.add(R2)
reds.add(R3)
reds.add(R4)
reds.add(R5)
reds.add(R6)
reds.add(R7)
reds.add(R8)
reds.add(R9)

entities.add(P1)

entities.add(R0)
entities.add(R1)
entities.add(R2)
entities.add(R3)
entities.add(R4)
entities.add(R5)
entities.add(R6)
entities.add(R7)
entities.add(R8)
entities.add(R9)

entities.add(G1)
entities.add(G2)
entities.add(G3)
entities.add(G4)
entities.add(G5)


while is_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_going = False
    screen.fill(WHITE)
    if SCORE < 0:
        screen.blit(pygame.image.load('icons/over.png'), (0, 0))
        pygame.mixer.music.stop()
        for entity in entities:
            entity.kill()
        pygame.display.flip()
        time.sleep(2)
        is_going = False
    for entity in entities:
        entity.move()
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollide(P1, reds, dokill=True):
        SCORE -= 1
    if pygame.sprite.spritecollide(P1, greens, dokill=True):
        SCORE += 1
    screen.blit(FONT.render('Score:', True, ORANGE), (650, 20))
    screen.blit(FONT.render(f'{SCORE}', True, ORANGE), (720, 20))

    if R0 not in reds:
        R0 = Red()
        reds.add(R0)
        entities.add(R0)
    if R1 not in reds:
        R1 = Red()
        reds.add(R1)
        entities.add(R1)
    if R2 not in reds:
        R2 = Red()
        reds.add(R2)
        entities.add(R2)
    if R3 not in reds:
        R3 = Red()
        reds.add(R3)
        entities.add(R3)
    if R4 not in reds:
        R4 = Red()
        reds.add(R4)
        entities.add(R4)
    if R5 not in reds:
        R5 = Red()
        reds.add(R5)
        entities.add(R5)
    if R6 not in reds:
        R6 = Red()
        reds.add(R6)
        entities.add(R6)
    if R7 not in reds:
        R7 = Red()
        reds.add(R7)
        entities.add(R7)
    if R8 not in reds:
        R8 = Red()
        reds.add(R8)
        entities.add(R8)
    if R9 not in reds:
        R9 = Red()
        reds.add(R9)
        entities.add(R9)
    if G1 not in greens:
        G1 = Green()
        greens.add(G1)
        entities.add(G1)
    if G2 not in greens:
        G2 = Green()
        greens.add(G2)
        entities.add(G2)
    if G3 not in greens:
        G3 = Green()
        greens.add(G3)
        entities.add(G3)
    if G4 not in greens:
        G4 = Green()
        greens.add(G4)
        entities.add(G4)
    if G5 not in greens:
        G5 = Green()
        greens.add(G5)
        entities.add(G5)



    pygame.display.flip()
    clock.tick(60)
pygame.quit()
