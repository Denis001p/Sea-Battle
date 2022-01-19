import pygame


def main(sc1, sc2, f1, f2, p1, p2):
    pygame.init()
    size = width, height = 700, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))
            if sc1>sc2:
                screen.blit(pygame.font.Font(None, 60).render(f'{p1} - победитель!', True, 'white'), (120, 110))
            elif sc2>sc1:
                screen.blit(pygame.font.Font(None, 60).render(f'{p2} - победитель!', True, 'white'), (120, 110))

            screen.blit(pygame.font.Font(None, 40).render(f'{p1}', True, 'white'), (150, 200))
            screen.blit(pygame.font.Font(None, 40).render(f'{sc1}', True, 'white'), (180, 255))
            screen.blit(pygame.font.Font(None, 40).render(f'{f1}', True, 'red'), (185, 290))

            screen.blit(pygame.font.Font(None, 40).render(f'{p2}', True, 'white'), (400, 200))
            screen.blit(pygame.font.Font(None, 40).render(f'{sc2}', True, 'white'), (430, 255))
            screen.blit(pygame.font.Font(None, 40).render(f'{f2}', True, 'red'), (435, 290))


        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
