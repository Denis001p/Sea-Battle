import pygame
from board import Board


def main():
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Настройки')
    running = True

    background1 = Board(50, 50)
    background1.set_view(-20, -20, 30)
    background2 = Board(50, 50)
    background2.set_view(-19, -21, 30)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
            screen.fill('#7092be')
            background2.render(screen, '#888888', 1)
            background1.render(screen, '#7092be', 1)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
