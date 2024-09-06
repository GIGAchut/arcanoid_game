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

def show_records(screen):
    font1 = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 74)  # Используем шрифт, аналогичный меню
    button_font = pygame.font.Font(None, 50)

    # Читаем рекорды каждый раз при вызове функции
    def load_scores(filename='records.txt'):
        with open(filename, 'r') as file:
            scores = [line.strip() for line in file]
        return scores

    def show_score(scores):
        y = 200
        yy = 200
        i = 1
        for item in scores:
            if i <= 5:
                draw_text(screen, f'{i}: {item}', font2, BLACK, 200, y)
                y += 50
            else:
                draw_text(screen, f'{i}: {item}', font2, BLACK, 500, yy)
                yy += 50
            i += 1
    while True:
        scores = load_scores()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if back1_button.collidepoint(mouse_x, mouse_y):
                    return "back_menu"

        screen.fill((0, 255, 255))  # Цвет фона

        draw_text(screen, 'Рекорды', font2, BLACK, 270, 100)

        show_score(scores)

        back1_button = pygame.Rect(300, 500, 200, 50)
        draw_button(screen, 'Назад', button_font, (0, 0, 0), back1_button, (0, 0, 0))

        pygame.display.update()




