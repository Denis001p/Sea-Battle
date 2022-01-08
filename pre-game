import os
import sys
import pygame
from board import Board
FORM = {4: [(360, 90)],
        3: [(360, 130), (460, 130)],
        2: [(360, 170), (430, 170), (500, 170)],
        1: [(360, 210), (400, 210), (440, 210), (480, 210)]}


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
        self.m = m
        self.r = False
        self.size = (30*n, 30)
        self.image = pygame.transform.scale(load_image(f'1x{n}.png'), self.size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = FORM[n][m]
        self.aura = pygame.Rect(self.rect.x-25, self.rect.y-25, 30*n+50, 80)

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
            self.aura = pygame.Rect(self.rect.x-25, self.rect.y-25, 80, 30*self.n+50)
        else:
            self.aura = pygame.Rect(self.rect.x-25, self.rect.y-25, 30*self.n+50, 80)

    def update(self, *args):
        pass


def main(username, first):
    pygame.init()
    size = width, height = 700, 475
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True
    draw = False

    background1 = Board(50, 50)
    background1.set_view(-20, -20, 30)
    background2 = Board(50, 50)
    background2.set_view(-19, -21, 30)
    mainboard = Board(10, 10)
    mainboard.set_view(80, 20, 30)
    shipboard = pygame.Rect((350, 80), (300, 300))
    cont = pygame.Rect((350, 395), (300, 60))

    ships = pygame.sprite.Group()
    Ship(4, 0, ships)
    Ship(3, 0, ships), Ship(3, 1, ships)
    Ship(2, 0, ships), Ship(2, 1, ships), Ship(2, 2, ships)
    Ship(1, 0, ships), Ship(1, 1, ships), Ship(1, 2, ships), Ship(1, 3, ships)

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
                        if not (nxy and ((nxy[0] + ship.n < 11 and not ship.r) or (nxy[1] + ship.n < 11 and ship.r)))\
                                or (ship.rect.x, ship.rect.y) not in [(i*30+20, j*30+80) for j in range(10) for i in range(10)]\
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
            if event.type == pygame.MOUSEMOTION:
                delta = event.rel
                x, y = event.pos
                if draw:
                    ship.image.set_alpha(175)
                    ship.rect.x += delta[0]
                    ship.rect.y += delta[1]
                    nxy = mainboard.get_cell((x, y))
                    if nxy and ((nxy[0] + ship.n < 11 and not ship.r) or (nxy[1] + ship.n < 11 and ship.r)) and\
                            not [True for el in ships if el.aura.colliderect(ship.rect) and el != ship]:
                        ship.rect.x = 20 + nxy[0] * 30
                        ship.rect.y = 80 + nxy[1] * 30
                    ship.aura.x, ship.aura.y = ship.rect.x - 25, ship.rect.y - 25
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if draw:
                    ship.rotate()
            screen.fill('#7092be')
            background2.render(screen, '#888888', 1)
            background1.render(screen, '#7092be', 1)
            mainboard.render(screen, 'white', 2)
            pygame.draw.rect(screen, 'black', shipboard, 1)
            pygame.draw.rect(screen, '#3f48cc', cont, 0)
            pygame.draw.rect(screen, 'black', ((350, 395), (300, 60)), 2)
            screen.blit(pygame.font.Font(None, 55).render(f'{username}, приготовьте флот!', True, 'white'), (20, 20))
            screen.blit(pygame.font.Font(None, 40).render('Продолжить', True, 'white'), (410, 412)) if first else screen.blit(pygame.font.Font(None, 50).render('В бой!', True, 'white'), (445, 412))
            ships.draw(screen)
        pygame.display.flip()
    pygame.quit()
    for i in range(10):
        for j in range(10):
            for el in ships:
                if el.rect.collidepoint(20+i*30, 80+j*30):
                    mainboard.board[j][i] = 1
    return mainboard.board


if __name__ == '__main__':
    PLACEMENT1 = main('Игрок 1', 1)
    PLACEMENT2 = main('Игрок 2', 0)
    from pprint import pprint
    pprint(PLACEMENT1)
    print('----------------------------------------------')
    pprint(PLACEMENT2)
