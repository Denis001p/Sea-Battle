import pygame


def main(win):
    pygame.init()
    size = width, height = 600, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True
    wl, d1, d2 = win
    winr, losr = wl

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))
            screen.blit(pygame.font.Font(None, 60).render(f'{winr} победил!', True, 'white'), (120, 50))
            screen.blit(pygame.font.Font(None, 40).render('Уничтожено кораблей:', True, 'red'), (140, 150))

            screen.blit(pygame.font.Font(None, 40).render(f'{winr}', True, 'white'), (120, 200))
            screen.blit(pygame.font.Font(None, 40).render(f'{d2}', True, 'red'), (165, 255))

            screen.blit(pygame.font.Font(None, 40).render(f'{losr}', True, 'white'), (350, 200))
            screen.blit(pygame.font.Font(None, 40).render(f'{d1}', True, 'red'), (395, 255))

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main((('Игрок 1', 'Игрок 2'), 2, 0))
