import pygame
from board import Board
from pregame import load_image
from random import choice


misses = pygame.sprite.Group()
shots = pygame.sprite.Group()


class MissSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(misses)
        self.image = pygame.transform.scale(load_image('missprint.png'), (30, 30))
        self.rect = pygame.Rect((x, y), (30, 30))


class ShotSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(shots)
        self.image = pygame.transform.scale(load_image('shotprint.png'), (30, 30))
        self.rect = pygame.Rect((x, y), (30, 30))


def main(p1, p2, plsh1, plsh2):
    pygame.init()
    size = width, height = 825, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True
    clock = pygame.time.Clock()
    curr_move = 1

    destroyed1 = []
    destroyed2 = []

    pl1, sh1 = plsh1
    pl2, sh2 = plsh2
    mainboard1 = Board(10, 10)
    mainboard1.set_view(110, 50, 30)
    mainboard1.board = pl2
    mainboard2 = Board(10, 10)
    mainboard2.set_view(110, 450, 30)
    mainboard2.board = pl1

    ships1 = [ship for ship in sh2 if ship.type == 'ship']
    mines1 = [ship for ship in sh2 if ship.type == 'mine']
    ships2 = [ship for ship in sh1 if ship.type == 'ship']
    mines2 = [ship for ship in sh1 if ship.type == 'mine']

    hit = False
    hitm = False
    hitms = False
    coord = ''
    x, y = 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hit = False
                hitm = False
                hitms = False
                coord = ''
                x, y = 0, 0
                if curr_move == 1:
                    if pygame.Rect((50, 110), (300, 300)).collidepoint(event.pos):
                        i, j = mainboard1.get_cell(event.pos)
                        cell = mainboard1.board[j][i]
                        x, y = 50 + 30 * i, 110 + 30 * j
                        if cell == '.':
                            MissSprite(x, y)
                            continue
                        elif cell == 0:
                            mainboard1.board[j][i] = '.'
                            MissSprite(x, y)
                            curr_move = 2
                        else:
                            hit = True
                            mainboard1.board[j][i] = 'X'
                            ShotSprite(x, y)
                            for el in sh2:
                                for c in el.coords:
                                    if c == (j, i):
                                        abc = 'ABCDEFGHIJ'
                                        if el.type == 'mine':
                                            curr_move = 2
                                            hitm = True
                                            if ships2:
                                                try:
                                                    coord = choice(choice(ships2).coords)
                                                    coord = f'На {abc[coord[1]] + str(coord[0] + 1)} есть корабль врага!'
                                                except:
                                                    coord = ''
                                        elif el.type == 'minesweeper':
                                            curr_move = 2
                                            hitms = True
                                            if mines2:
                                                try:
                                                    coord = choice(choice(mines2).coords)
                                                    coord = f'На {abc[coord[1]] + str(coord[0] + 1)} есть мина врага!'
                                                except:
                                                    coord = ''
                                        el.coords.remove(c)
                                        if not el.coords:
                                            destroyed1.append(el)
                                            for jj, ii in el.auracoords:
                                                mainboard1.board[jj][ii] = '.'
                                                MissSprite(50 + 30 * ii, 110 + 30 * jj)
                                            if set(ships1) == set(destroyed1):
                                                running = False
                                            continue
                                        continue

                else:
                    if pygame.Rect((450, 110), (300, 300)).collidepoint(event.pos):
                        i, j = mainboard2.get_cell(event.pos)
                        cell = mainboard2.board[j][i]
                        x, y = 450 + 30 * i, 110 + 30 * j
                        if cell == '.':
                            MissSprite(x, y)
                            continue
                        elif cell == 0:
                            mainboard2.board[j][i] = '.'
                            MissSprite(x, y)
                            curr_move = 1
                        else:
                            hit = True
                            mainboard2.board[j][i] = 'X'
                            ShotSprite(x, y)
                            for el in sh1:
                                for c in el.coords:
                                    if c == (j, i):
                                        abc = 'ABCDEFGHIJ'
                                        if el.type == 'mine':
                                            curr_move = 1
                                            hitm = True
                                            if ships1:
                                                try:
                                                    coord = choice(choice(ships1).coords)
                                                    coord = f'На {abc[coord[1]] + str(coord[0] + 1)} есть корабль врага!'
                                                except:
                                                    coord = ''
                                        elif el.type == 'minesweeper':
                                            curr_move = 1
                                            hitms = True
                                            if mines1:
                                                try:
                                                    coord = choice(choice(mines1).coords)
                                                    coord = f'На {abc[coord[1]] + str(coord[0] + 1)} есть мина врага!'
                                                except:
                                                    coord = ''
                                        el.coords.remove(c)
                                        if not el.coords:
                                            destroyed2.append(el)
                                            for jj, ii in el.auracoords:
                                                mainboard2.board[jj][ii] = '.'
                                                MissSprite(450+30*ii, 110+30*jj)
                                            if set(ships2) == set(destroyed2):
                                                running = False
                                            continue
                                        continue
            screen.blit(load_image('background.jpg'), (0, 0))
            mainboard1.render(screen, 'white', 2)
            mainboard2.render(screen, 'white', 2)

            screen.blit(pygame.font.Font(None, 40).render('A', True, 'white'), (450, 80))
            screen.blit(pygame.font.Font(None, 40).render('B', True, 'white'), (480, 80))
            screen.blit(pygame.font.Font(None, 40).render('C', True, 'white'), (510, 80))
            screen.blit(pygame.font.Font(None, 40).render('D', True, 'white'), (540, 80))
            screen.blit(pygame.font.Font(None, 40).render('E', True, 'white'), (570, 80))
            screen.blit(pygame.font.Font(None, 40).render('F', True, 'white'), (600, 80))
            screen.blit(pygame.font.Font(None, 40).render('G', True, 'white'), (630, 80))
            screen.blit(pygame.font.Font(None, 40).render('H', True, 'white'), (660, 80))
            screen.blit(pygame.font.Font(None, 40).render('I', True, 'white'), (690, 80))
            screen.blit(pygame.font.Font(None, 40).render('J', True, 'white'), (720, 80))
            screen.blit(pygame.font.Font(None, 40).render('1', True, 'white'), (420, 110))
            screen.blit(pygame.font.Font(None, 40).render('2', True, 'white'), (420, 140))
            screen.blit(pygame.font.Font(None, 40).render('3', True, 'white'), (420, 170))
            screen.blit(pygame.font.Font(None, 40).render('4', True, 'white'), (420, 200))
            screen.blit(pygame.font.Font(None, 40).render('5', True, 'white'), (420, 230))
            screen.blit(pygame.font.Font(None, 40).render('6', True, 'white'), (420, 260))
            screen.blit(pygame.font.Font(None, 40).render('7', True, 'white'), (420, 290))
            screen.blit(pygame.font.Font(None, 40).render('8', True, 'white'), (420, 320))
            screen.blit(pygame.font.Font(None, 40).render('9', True, 'white'), (420, 350))
            screen.blit(pygame.font.Font(None, 40).render('10', True, 'white'), (420, 380))

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

            p = p2 if curr_move == 2 else p1
            if hit:
                pygame.draw.rect(screen, 'red', ((x, y), (30, 30)), 0)
            if hitm:
                screen.blit(pygame.font.Font(None, 40).render(f'{p}, ваша мина сработала!', True, 'white'), (20, 420))
                if coord:
                    screen.blit(pygame.font.Font(None, 40).render(coord, True, 'white'), (20, 450))
            if hitms:
                screen.blit(pygame.font.Font(None, 40).render(f'{p}, ваш минный тральщик сработал!', True, 'white'),
                            (20, 420))
                if coord:
                    screen.blit(pygame.font.Font(None, 40).render(coord, True, 'white'), (20, 450))

            misses.draw(screen)
            shots.draw(screen)

            if curr_move == 1:
                screen.blit(pygame.font.Font(None, 55).render(f'{p1}, ваш ход!', True, 'white'), (20, 20))
                pygame.draw.line(screen, 'blue', (50, 420), (350, 420), 5)
            else:
                screen.blit(pygame.font.Font(None, 55).render(f'{p2}, ваш ход!', True, 'white'), (20, 20))
                pygame.draw.line(screen, 'blue', (450, 420), (750, 420), 5)
        clock.tick(1000)
        pygame.display.flip()
    pygame.quit()

    return ((p1, p2) if curr_move == 1 else (p2, p1)), len(destroyed1), len(destroyed2)