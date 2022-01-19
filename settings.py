import pygame
import sqlite3


def main():
    pygame.init()
    size = width, height = 400, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Настройки')
    running = True

    cur = sqlite3.connect('settings.db').cursor()
    nick1 = cur.execute('SELECT nickname FROM nicknames WHERE id = 1').fetchone()[0]
    nick2 = cur.execute('SELECT nickname FROM nicknames WHERE id = 2').fetchone()[0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
