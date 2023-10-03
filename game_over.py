import pygame
def game_over_screen(screen):
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Очистка экрана (рисование белого фона)
        screen.fill((255, 255, 255))

        # Отображение окна "Game Over"
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Поражение", True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 50)
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font(None, 36)
        text_surface = font.render("Нажмите Enter для продолжения", True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

        # Добавляем проверку на нажатие Enter
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

