import pygame

def main_menu(screen):
    running = True
    clock = pygame.time.Clock()

    play_button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 - 25, 200, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_button_rect.collidepoint(event.pos):
                        running = False

        # Очистка экрана (рисование белого фона)
        screen.fill((255, 255, 255))

        # Отображение кнопки "Play"
        pygame.draw.rect(screen, (0, 128, 0), play_button_rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Play", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = play_button_rect.center
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)
