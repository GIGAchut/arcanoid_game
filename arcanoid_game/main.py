import pygame
import sys
from engine import run_game  # Импортируем функцию запуска игрового движка
from information import show_info  # Импортируем функцию отображения информации
from records import show_records
# Инициализация Pygame
pygame.init()
icon = pygame.image.load('favicon.ico')
pygame.display.set_icon(icon)
# Установка размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
BACKGROUND_COLOR = (0, 255, 255)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('ARCANOID')

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Инициализация шрифта
pygame.font.init()
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def draw_button(surface, text, font, color, rect, border_color):
    pygame.draw.rect(surface, border_color, rect, 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def show_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button.collidepoint(mouse_x, mouse_y):
                    return "start_game"
                elif records_button.collidepoint(mouse_x, mouse_y):
                    return "show_records"
                elif info_button.collidepoint(mouse_x, mouse_y):
                    return "show_info"
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        screen.fill(BACKGROUND_COLOR)
        draw_text(screen, 'АРКАНОИД', font, BLACK, WINDOW_WIDTH // 2 - 150, 100)

        start_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 250, 200, 50)
        records_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 350, 200, 50)
        info_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 450, 200, 50)
        quit_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 550, 200, 50)

        draw_button(screen, 'Начать игру', button_font, BLACK, start_button, BLACK)
        draw_button(screen, 'Рекорды', button_font, BLACK, records_button, BLACK)
        draw_button(screen, 'Об игре', button_font, BLACK, info_button, BLACK)
        draw_button(screen, 'Выйти', button_font, BLACK, quit_button, BLACK)

        pygame.display.update()

def main():

    while True:
        current_state = show_menu()

        if current_state == "start_game":
            next_state = run_game(screen)
            if next_state == "back_menu_of_game":
                continue
        elif current_state == "show_info":
            next_state = show_info(screen)  # Вызываем функцию из другого файла и передаем ей экран
            if next_state == "back_to_menu":
                continue  # Возвращаемся в меню
        elif current_state == "show_records":
            next_state = show_records(screen)
            if next_state == "back_menu":
                continue  # Возвращаемся в меню
        elif current_state == "quit":
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
