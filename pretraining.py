import pygame


def main():
    pygame.init()
    size = width, height = 250, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect((0, 0), (250, 200)).collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    if pygame.Rect((0, 0), (250, 50)).collidepoint(event.pos):
                        return 1
                    if pygame.Rect((0, 0), (250, 100)).collidepoint(event.pos):
                        return 2
                    if pygame.Rect((0, 0), (250, 150)).collidepoint(event.pos):
                        return 3
                    if pygame.Rect((0, 0), (250, 200)).collidepoint(event.pos):
                        return 'quit'
            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))
            pygame.draw.rect(screen, '#3f48cc', ((0, 0), (250, 200)), 0)
            pygame.draw.rect(screen, 'black', ((0, 0), (250, 50)), 3)
            pygame.draw.rect(screen, 'black', ((0, 0), (250, 100)), 3)
            pygame.draw.rect(screen, 'black', ((0, 0), (250, 150)), 3)
            pygame.draw.rect(screen, 'black', ((0, 0), (250, 200)), 3)
            screen.blit(pygame.font.Font(None, 40).render('Баржа', True, 'white'), (75, 12.5))
            screen.blit(pygame.font.Font(None, 40).render('Мина', True, 'white'), (80, 62.5))
            screen.blit(pygame.font.Font(None, 40).render('Тральщик', True, 'white'), (50, 112.5))
            screen.blit(pygame.font.Font(None, 40).render('Назад', True, 'white'), (75, 162.5))
        pygame.display.flip()
    pygame.quit()