import pygame
from board import Board
from game import MissSprite, ShotSprite
from random import choice


PLACEMENTS = {
    1: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    2: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    3: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
}


def main(lvl):
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True
    clock = pygame.time.Clock()
    curr_move = 1

    sh = []

    destroyed = []
    ships = [ship for ship in sh if ship.type == 'ship']
    mines = [ship for ship in sh if ship.type == 'mine']

    mainboard = Board(10, 10)
    mainboard.set_view(110, 50, 30)
    mainboard.board = PLACEMENTS[lvl]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for event in pygame.event.get():
                    hit = False
                    hitm = False
                    hitms = False
                    coord = ''
                    x, y = 0, 0
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.Rect((50, 110), (300, 300)).collidepoint(event.pos):
                            i, j = mainboard.get_cell(event.pos)
                            cell = mainboard.board[j][i]
                            x, y = 50 + 30 * i, 110 + 30 * j
                            if cell == '.':
                                MissSprite(x, y)
                                continue
                            elif cell == 0:
                                mainboard.board[j][i] = '.'
                                MissSprite(x, y)
                                curr_move = 2
                            else:
                                hit = True
                                mainboard.board[j][i] = 'X'
                                ShotSprite(x, y)
                                for el in sh:
                                    for c in el.coords:
                                        if c == (j, i):
                                            abc = 'ABCDEFGHIJ'
                                            if el.type == 'mine':
                                                hitm = True
                                                if ships:
                                                    coord = choice(choice(ships).coords)
                                                    coord = f'На {abc[coord[0]] + str(coord[1] + 1)} есть корабль врага!'
                                            elif el.type == 'minesweeper':
                                                hitms = True
                                                if mines:
                                                    coord = choice(choice(mines).coords)
                                                    coord = f'На {abc[coord[0]] + str(coord[1] + 1)} есть мина врага!'
                                            el.coords.remove(c)
                                            if not el.coords:
                                                destroyed1.append(el)
                                                for jj, ii in el.auracoords:
                                                    mainboard.board[jj][ii] = '.'
                                                    MissSprite(50 + 30 * ii, 110 + 30 * jj)
                                                if set(ships) == set(destroyed):
                                                    running = False
                                                continue
                                            continue

            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))

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

        pygame.display.flip()
    pygame.quit()
