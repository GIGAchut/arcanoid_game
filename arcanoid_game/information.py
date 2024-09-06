import pygame
import sys

BLACK = (0, 0, 0)

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def draw_button(surface, text, font, color, rect, border_color):
    pygame.draw.rect(surface, border_color, rect, 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def show_info(screen):
    font1 = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 74)  # Используем шрифт, аналогичный меню
    button_font = pygame.font.Font(None, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if back_button.collidepoint(mouse_x, mouse_y):
                    return "back_to_menu"

        screen.fill((0, 255, 255))  # Цвет фона

        draw_text(screen, 'Информация об игре', font2, BLACK, 125, 100)
        draw_text(screen, 'Игра арканоид', font1, BLACK, 15, 200)
        draw_text(screen, 'Цель игры - пройти 4 уровня, уничтожив все блоки', font1, BLACK, 15, 250)
        draw_text(screen, 'Управление осуществляется путём нажатия клавиш A и D', font1, BLACK, 15, 300)
        draw_text(screen, 'При выходе из игры, не закончив её (приоигрышем или', font1, BLACK, 15, 350)
        draw_text(screen, 'выигрышем), текущей результат будет потерян', font1, BLACK, 15, 400)


        back_button = pygame.Rect(300, 500, 200, 50)
        draw_button(screen, 'Назад', button_font, (0, 0, 0), back_button, (0, 0, 0))

        pygame.display.update()
