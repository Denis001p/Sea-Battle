import pygame


def main():
    pygame.init()
    size = width, height = 500, 500
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

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
