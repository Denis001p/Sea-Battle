import os
import sys
import pygame
import sqlite3
from board import Board
from settings import STNGS as db
FORM = {
    1: [(390 + i * 40, 210) for i in range(db[0])],
    2: [(390 + i * 70, 170) for i in range(db[1])],
    3: [(390 + i * 100, 130) for i in range(db[2])],
    4: [(390+i*130, 90) for i in range(db[3])],
    5: [(390+i*70, 250) for i in range(db[4])],
    6: [(390+i*40, 320) for i in range(db[5])],
    7: [(390+i*40, 360) for i in range(db[6])]
}


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Ship(pygame.sprite.Sprite):
    def __init__(self, n, m, group):
        super().__init__(group)
        self.n = n
        self.nn = n if n in (1, 2, 3, 4) else 1
        self.m = m
        self.r = False
        if n == 6:
            self.type = 'mine'
        elif n == 7:
            self.type = 'minesweeper'
        else:
            self.type = 'ship'
        self.isbase = 1
        self.coords = []
        self.auracoords = set()
        if n == 5:
            self.nn = 2
            self.isbase = 2
        self.size = (30*self.nn, 30*self.isbase)
        self.image = pygame.transform.scale(load_image(f'1x{n}.png'), self.size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = FORM[n][m]
        self.aura = pygame.Rect(self.rect.x-25, self.rect.y-25, 30*self.nn+50, 30*self.isbase+50)

    def rotate(self):
        x, y = self.rect.x, self.rect.y
        if not self.r:
            self.image = pygame.transform.rotate(self.image, -90)
            self.r = True
        elif self.r:
            self.image = pygame.transform.rotate(self.image, 90)
            self.r = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        if self.r:
            self.aura = pygame.Rect(self.rect.x-25, self.rect.y-25, 30*self.isbase+50, 30*self.nn+50)
        else:
            self.aura = pygame.Rect(self.rect.x-25, self.rect.y-25, 30*self.nn+50, 30*self.isbase+50)

    def update(self, *args):
        pass


def main(username, first):
    pygame.init()
    size = width, height = 725, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True
    draw = False

    mainboard = Board(10, 10)
    mainboard.set_view(110, 50, 30)
    shipboard = pygame.Rect((380, 80), (330, 330))
    cont = pygame.Rect((380, 425), (330, 60))
    stngs = pygame.Rect((20, 425), (60, 60))

    ships = pygame.sprite.Group()
    for i in FORM:
        for j in range(len(FORM[i])):
            Ship(i, j, ships)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainboard.get_click(event.pos)
                x, y = event.pos
                for el in ships:
                    if draw:
                        nxy = mainboard.get_cell((x, y))
                        if not (nxy and ((nxy[0] + ship.nn < 11 and not ship.r) or (nxy[1] + ship.nn < 11 and ship.r)))\
                                or (ship.rect.x, ship.rect.y) not in [(i*30+50, j*30+110) for j in range(10) for i in range(10)]\
                                or [True for el in ships if ship.rect.colliderect(el.rect) and ship != el]:
                            if ship.r:
                                ship.rotate()
                            ship.rect.x, ship.rect.y = FORM[ship.n][ship.m]
                            ship.aura.x, ship.aura.y = ship.rect.x - 25, ship.rect.y - 25
                        ship.image.set_alpha(9999)
                        draw = False
                        break
                    if el.rect.collidepoint(x, y):
                        ship = el
                        draw = True
                        break
                if cont.collidepoint(x, y):
                    if not any([True for el in ships if shipboard.contains(el.rect)]):
                        running = False
                    else:
                        screen.blit(pygame.font.Font(None, 55).render(f'{username}, приготовьте флот!', True, 'red'),
                                    (20, 20))
                        pygame.time.Clock().tick(5)
                        pygame.display.flip()
                if stngs.collidepoint(x, y):
                    pygame.quit()
                    raise ConnectionRefusedError
            if event.type == pygame.MOUSEMOTION:
                delta = event.rel
                x, y = event.pos
                if draw:
                    ship.image.set_alpha(175)
                    ship.rect.x += delta[0]
                    ship.rect.y += delta[1]
                    nxy = mainboard.get_cell((x, y))
                    if nxy and ((nxy[0] + ship.nn < 11 and not ship.r and not ship.n == 5) or
                                (nxy[1] + ship.nn < 11 and ship.r and not ship.n == 5)
                                or (nxy[1] + ship.nn < 11 and ship.n == 5)) and\
                            not [True for el in ships if el.aura.colliderect(ship.rect) and el != ship]:
                        ship.rect.x = 50 + nxy[0] * 30
                        ship.rect.y = 110 + nxy[1] * 30
                    ship.aura.x, ship.aura.y = ship.rect.x - 25, ship.rect.y - 25
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if draw:
                    ship.rotate()
            screen.blit(load_image('background.jpg'), (0, 0))
            mainboard.render(screen, 'white', 2)

            screen.blit(pygame.font.Font(None, 40).render('A', True, 'white'), (50, 80))
            screen.blit(pygame.font.Font(None, 40).render('B', True, 'white'), (80, 80))
            screen.blit(pygame.font.Font(None, 40).render('C', True, 'white'), (110, 80))
            screen.blit(pygame.font.Font(None, 40).render('D', True, 'white'), (140, 80))
            screen.blit(pygame.font.Font(None, 40).render('E', True, 'white'), (170, 80))
            screen.blit(pygame.font.Font(None, 40).render('F', True, 'white'), (200, 80))
            screen.blit(pygame.font.Font(None, 40).render('G', True, 'white'), (230, 80))
            screen.blit(pygame.font.Font(None, 40).render('H', True, 'white'), (260, 80))
            screen.blit(pygame.font.Font(None, 40).render('I', True, 'white'), (290, 80))
            screen.blit(pygame.font.Font(None, 40).render('J', True, 'white'), (320, 80))
            screen.blit(pygame.font.Font(None, 40).render('1', True, 'white'), (20, 110))
            screen.blit(pygame.font.Font(None, 40).render('2', True, 'white'), (20, 140))
            screen.blit(pygame.font.Font(None, 40).render('3', True, 'white'), (20, 170))
            screen.blit(pygame.font.Font(None, 40).render('4', True, 'white'), (20, 200))
            screen.blit(pygame.font.Font(None, 40).render('5', True, 'white'), (20, 230))
            screen.blit(pygame.font.Font(None, 40).render('6', True, 'white'), (20, 260))
            screen.blit(pygame.font.Font(None, 40).render('7', True, 'white'), (20, 290))
            screen.blit(pygame.font.Font(None, 40).render('8', True, 'white'), (20, 320))
            screen.blit(pygame.font.Font(None, 40).render('9', True, 'white'), (20, 350))
            screen.blit(pygame.font.Font(None, 40).render('10', True, 'white'), (20, 380))

            pygame.draw.rect(screen, 'black', shipboard, 1)
            pygame.draw.rect(screen, '#3f48cc', cont, 0)
            pygame.draw.rect(screen, 'black', cont, 2)
            pygame.draw.rect(screen, '#3f48cc', stngs, 0)
            pygame.draw.rect(screen, 'black', stngs, 2)
            screen.blit(pygame.font.Font(None, 55).render(f'{username}, приготовьте флот!', True, 'white'), (20, 20))
            screen.blit(pygame.font.Font(None, 25).render('R - повернуть корабль', True, 'white'), (125, 430))
            screen.blit(pygame.font.Font(None, 45).render('Продолжить', True, 'white'), (450, 442)) if first else screen.blit(pygame.font.Font(None, 50).render('В бой!', True, 'white'), (485, 442))
            screen.blit(pygame.transform.scale(load_image('stngs.png'), (50, 50)), (25, 430))
            ships.draw(screen)
        pygame.display.flip()
    pygame.quit()
    for i in range(10):
        for j in range(10):
            for el in ships:
                if el.aura.collidepoint(65+i*30, 125+j*30) and not el.rect.collidepoint(50+i*30, 110+j*30):
                    el.auracoords.add((j, i))
                if el.rect.collidepoint(50+i*30, 110+j*30):
                    mainboard.board[j][i] = el.n
                    el.coords.append((j, i))

    return mainboard.board, ships
