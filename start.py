import pygame


def main():
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Морской бой')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect((175, 150), (250, 200)).collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    if pygame.Rect((175, 150), (250, 50)).collidepoint(event.pos):
                        return 'start'
                    if pygame.Rect((175, 150), (250, 100)).collidepoint(event.pos):
                        return 'training'
                    if pygame.Rect((175, 150), (250, 150)).collidepoint(event.pos):
                        return 'settings'
                    if pygame.Rect((175, 150), (250, 200)).collidepoint(event.pos):
                        return 'quit'
            screen.blit(pygame.image.load('data/background.jpg'), (0, 0))
            screen.blit(pygame.font.Font(None, 80).render('МОРСКОЙ БОЙ', True, 'white'), (90, 60))
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/1x4.png'), (180, 45)), -90), (75, 150))
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/1x4.png'), (180, 45)), -90), (480, 150))
            pygame.draw.rect(screen, '#3f48cc', ((175, 150), (250, 200)), 0)
            pygame.draw.rect(screen, 'black', ((175, 150), (250, 50)), 3)
            pygame.draw.rect(screen, 'black', ((175, 150), (250, 100)), 3)
            pygame.draw.rect(screen, 'black', ((175, 150), (250, 150)), 3)
            pygame.draw.rect(screen, 'black', ((175, 150), (250, 200)), 3)
            screen.blit(pygame.font.Font(None, 40).render('Играть', True, 'white'), (250, 162.5))
            screen.blit(pygame.font.Font(None, 40).render('Тренировка', True, 'white'), (220, 212.5))
            screen.blit(pygame.font.Font(None, 40).render('Настройки', True, 'white'), (225, 262.5))
            screen.blit(pygame.font.Font(None, 40).render('Выход', True, 'white'), (250, 312.5))
        pygame.display.flip()
