import pygame
import random
import menu  # Импортируем модуль меню
import win  # Импортируем модуль win
import game_over  # Импортируем модуль game_over



# Инициализация Pygame
pygame.init()

target_score = 10
# Определение размеров окна
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Arcade project")

# Отображение главного меню
menu.main_menu(screen)

# Инициализация переменных
player_rect = pygame.Rect(WIDTH // 2 - 20, HEIGHT - 30, 40, 10)
score = 0
lives = 3


# Создание списков для объектов
good_objects = []
bad_objects = []

# Функция для создания новых объектов с задержкой
last_good_object_time = 0
last_bad_object_time = 0

def create_objects():
    global last_good_object_time, last_bad_object_time

    current_time = pygame.time.get_ticks()

    # Создавать новые объекты с интервалом
    if current_time - last_good_object_time > 500:  # Задержка для хороших объектов (0.5 секунды)
        good_rect = pygame.Rect(random.randint(0, WIDTH - 30), 0, 30, 30)
        good_objects.append(good_rect)
        last_good_object_time = current_time

    if current_time - last_bad_object_time > 1000:  # Задержка для плохих объектов (1 секунды)
        bad_rect = pygame.Rect(random.randint(0, WIDTH - 30), 0, 30, 30)
        bad_objects.append(bad_rect)
        last_bad_object_time = current_time

# Главный цикл игры
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    # Очистка экрана (рисование белого фона)
    screen.fill(WHITE)

    # Проверка на столкновения
    for good_rect in good_objects:
        good_rect.y += 5
        pygame.draw.rect(screen, GREEN, good_rect)
        if good_rect.colliderect(player_rect):
            good_objects.remove(good_rect)
            score += 1

    for bad_rect in bad_objects:
        bad_rect.y += 5
        pygame.draw.rect(screen, RED, bad_rect)
        if bad_rect.colliderect(player_rect):
            bad_objects.remove(bad_rect)
            lives -= 1

    # Создание новых объектов с задержкой
    create_objects()

    # Отображение текста
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Score: {score}", True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (20, 20)
    screen.blit(text_surface, text_rect)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Lives: {lives}", True, RED)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (WIDTH - 140, 20)
    screen.blit(text_surface, text_rect)

    # Отображение игрока
    pygame.draw.rect(screen, BLUE, player_rect)

    # Обновление экрана
    pygame.display.flip()

    # Проверка на завершение игры
    if lives <= 0:
        running = False
    elif score >= target_score:
        running = False
# Проверка на завершение игры (пример)
if lives <= 0:
    game_over.game_over_screen(screen)  # Отображаем окно "Game Over"
# Проверка на победу (пример)
if score == target_score:
    win.win_screen(screen)  # Отображаем окно "Win"

pygame.display.flip()
clock.tick(60)

# Завершение игры
pygame.quit()