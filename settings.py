import pygame
import sqlite3


def insert_nick(data, id):
    con = sqlite3.connect('settings.db')
    con.cursor().execute(f'UPDATE nicknames SET nickname = {data} WHERE id = {id}')
    con.commit()


def main():
    pygame.init()
    size = width, height = 400, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Настройки')
    running = True

    con = sqlite3.connect('settings.db')
    cur = con.cursor()
    nick1 = cur.execute('SELECT nickname FROM nicknames WHERE id = 1').fetchone()[0]
    nick2 = cur.execute('SELECT nickname FROM nicknames WHERE id = 2').fetchone()[0]
    sh = [cur.execute('SELECT quantity FROM ships WHERE id = 1').fetchone()[0],
          cur.execute('SELECT quantity FROM ships WHERE id = 2').fetchone()[0],
          cur.execute('SELECT quantity FROM ships WHERE id = 3').fetchone()[0],
          cur.execute('SELECT quantity FROM ships WHERE id = 4').fetchone()[0],
          cur.execute('SELECT quantity FROM ships WHERE id = 5').fetchone()[0],
          cur.execute('SELECT quantity FROM ships WHERE id = 6').fetchone()[0],
          cur.execute('SELECT quantity FROM ships WHERE id = 7').fetchone()[0]]
    arrows = [pygame.Rect((160, 90), (20, 30)),
              pygame.Rect((205, 90), (20, 30)),
              pygame.Rect((160, 130), (20, 30)),
              pygame.Rect((205, 130), (20, 30)),
              pygame.Rect((160, 170), (20, 30)),
              pygame.Rect((205, 170), (20, 30)),
              pygame.Rect((160, 210), (20, 30)),
              pygame.Rect((205, 210), (20, 30)),
              pygame.Rect((160, 250), (20, 30)),
              pygame.Rect((205, 250), (20, 30)),
              pygame.Rect((160, 290), (20, 30)),
              pygame.Rect((205, 290), (20, 30)),
              pygame.Rect((290, 330), (20, 30)),
              pygame.Rect((330, 330), (20, 30))]

    back = pygame.Rect((190, 540), (200, 50))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    running = False
                for i in range(14):
                    if arrows[i].collidepoint(event.pos):
                        if i % 2 == 0:
                            zn = '-'
                        else:
                            zn = '+'
                        d = i // 2
                        now = sh[d] + 1 if zn == '+' else sh[d] - 1
                        border = (8, 4, 3, 2, 4, 8, 8)
                        if 0 <= now <= border[d]:
                            cur.execute(f'UPDATE ships SET quantity = {str(now)} WHERE id = {d + 1}')
                            con.commit()
            sh = [cur.execute('SELECT quantity FROM ships WHERE id = 1').fetchone()[0],
                  cur.execute('SELECT quantity FROM ships WHERE id = 2').fetchone()[0],
                  cur.execute('SELECT quantity FROM ships WHERE id = 3').fetchone()[0],
                  cur.execute('SELECT quantity FROM ships WHERE id = 4').fetchone()[0],
                  cur.execute('SELECT quantity FROM ships WHERE id = 5').fetchone()[0],
                  cur.execute('SELECT quantity FROM ships WHERE id = 6').fetchone()[0],
                  cur.execute('SELECT quantity FROM ships WHERE id = 7').fetchone()[0]]
            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))
            pygame.draw.rect(screen, '#3f48cc', back, 0)
            pygame.draw.rect(screen, 'black', back, 3)
            for rect in arrows:
                pygame.draw.rect(screen, '#3f48cc', rect, 0)
                pygame.draw.rect(screen, 'black', rect, 2)
            screen.blit(pygame.font.Font(None, 40).render('Назад', True, 'white'), (245, 552.5))
            screen.blit(pygame.font.Font(None, 40).render(f'Игрок 1: {nick1}', True, 'white'), (10, 10))
            screen.blit(pygame.font.Font(None, 40).render(f'Игрок 2: {nick2}', True, 'white'), (10, 50))
            screen.blit(pygame.font.Font(None, 40).render(f'Катеры:        {sh[0]}', True, 'white'), (10, 90))
            screen.blit(pygame.font.Font(None, 40).render(f'Эсминцы:     {sh[1]}', True, 'white'), (10, 130))
            screen.blit(pygame.font.Font(None, 40).render(f'Крейсеры:    {sh[2]}', True, 'white'), (10, 170))
            screen.blit(pygame.font.Font(None, 40).render(f'Линкоры:      {sh[3]}', True, 'white'), (10, 210))
            screen.blit(pygame.font.Font(None, 40).render(f'Баржи:          {sh[4]}', True, 'white'), (10, 250))
            screen.blit(pygame.font.Font(None, 40).render(f'Мины:            {sh[5]}', True, 'white'), (10, 290))
            screen.blit(pygame.font.Font(None, 40).render(f'Минные тральщики:    {sh[6]}', True, 'white'), (10, 330))
        pygame.display.flip()
    pygame.quit()