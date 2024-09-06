import pygame
import sys
from levels import create_level

# Параметры игры
BACKGROUND_COLOR = (0, 255, 255)
FPS = 60
total_level = 4

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def draw_button(surface, text, font, color, rect, border_color):
    pygame.draw.rect(surface, border_color, rect, 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def run_game(screen):
    clock = pygame.time.Clock()
    score = 0
    level = 1
    game_started = False  # Флаг, чтобы знать, началась ли игра

    class Area:
        def __init__(self, x=0, y=0, width=10, height=10):
            self.rect = pygame.Rect(x, y, width, height)

        def colliderect(self, rect):
            return self.rect.colliderect(rect)

    class Picture(Area):
        def __init__(self, x=0, y=0, width=50, height=50, filename='img/enemy.png'):
            super().__init__(x, y, width, height)
            self.image = pygame.image.load(filename)
            self.image = pygame.transform.scale(self.image, (width, height))  # Масштабируем изображение

        def draw(self):
            screen.blit(self.image, self.rect.topleft)

    game_run = True
    while game_run:

        monsters = create_level(level, screen, Picture)
        platform = Picture(350, 650, 100, 20, 'img/platform.png')
        ball = Picture(400, 300, 20, 20, 'img/ball.png')

        game = True
        run = True
        move_right, move_left = False, False
        speed_x, speed_y = 0, 0

        def display_score_and_level(screen, score, level):
            font = pygame.font.SysFont('verdana', 30)
            score_text = font.render(f'Score: {score}', True, (0, 0, 0))
            level_text = font.render(f'Level: {level}', True, (0, 0, 0))
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (650, 10))

        # Функция сохранения лучших рекордов в файл, топ 10
        def update_highscores(score, filename='records.txt'):
            with open(filename, 'r') as file:
                scores = [int(line.strip()) for line in file]
            scores.append(score)
            scores = sorted(scores, reverse=True)[:10]
            with open(filename, 'w') as file:
                for item in scores:
                    file.write(f"{item}\n")

        while run:
            clock.tick(FPS)
            if ball.rect.y > platform.rect.y:
                font1 = pygame.font.SysFont('verdana', 40)
                text = font1.render('YOU LOSE', True, (255, 0, 0))
                screen.blit(text, (300, 350))
                pygame.display.update()
                if game:
                    update_highscores(score)  # Сохранение только один раз
                    game = False

            if len(monsters) == 0:
                font1 = pygame.font.SysFont('verdana', 40)
                text = font1.render('YOU WIN!!!', True, (255, 0, 0))
                pygame.display.update()
                if level > 4:
                    screen.blit(text, (300, 350))
                    pygame.display.update()
                    if game:
                        update_highscores(score)  # Сохранение только один раз
                        game = False
                else:
                    level += 1
                    game_started = False
                    break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not game_started:
                        speed_x, speed_y = 5, 5  # Устанавливаем скорость мяча только один раз
                        game_started = True  # Устанавливаем флаг, что игра началась
                    if event.key == pygame.K_a:
                        move_left = True
                    if event.key == pygame.K_d:
                        move_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        move_left = False
                    if event.key == pygame.K_d:
                        move_right = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if back_button_of_game.collidepoint(mouse_x, mouse_y):
                        return "back_menu_of_game"

            if game:
                screen.fill(BACKGROUND_COLOR)
                button_font = pygame.font.Font(None, 50)
                back_button_of_game = pygame.Rect(300, 10, 200, 50)
                draw_button(screen, 'Назад', button_font, (0, 0, 0), back_button_of_game, (0, 0, 0))

                if game_started:  # Движение мяча только если игра началась
                    ball.rect.x += speed_x
                    ball.rect.y += speed_y

                if move_left and platform.rect.left > 0:
                    platform.rect.x -= 8
                if move_right and platform.rect.right < 800:
                    platform.rect.x += 8

                # Отскок от границ экрана
                if ball.rect.x >= 780 or ball.rect.x <= 0:
                    speed_x *= -1
                if ball.rect.y <= 0:
                    speed_y *= -1

                # Столкновение с платформой
                if ball.colliderect(platform.rect):
                    if ball.rect.bottom >= platform.rect.top and speed_y > 0:
                        speed_y *= -1
                        ball_center = ball.rect.centerx
                        platform_center = platform.rect.centerx
                        offset = ball_center - platform_center
                        speed_x = (offset // 10)  # Скорость по X зависит от точки касания мяча с платформой

                ball.draw()
                platform.draw()

                for monster in monsters:
                    if ball.colliderect(monster.rect):
                        monsters.remove(monster)
                        speed_y *= -1
                        score += 1
                    else:
                        monster.draw()
                display_score_and_level(screen, score, level)

            if not game_started and level <= 4:
                font2 = pygame.font.SysFont('verdana', 40)
                text = font2.render('Нажмите пробел для начала игры', True, (255, 0, 0))
                screen.blit(text, (50, 350))

            pygame.display.update()


