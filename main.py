import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img_lib/target.jpg")
pygame.display.set_icon(icon)

target = pygame.image.load("img_lib/targ.png")
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменные для подсчета попаданий, успешных и неудачных попыток, а также перемещений мишени
total_attempts = 0
successful_attempts = 0
failed_attempts = 0
moves = 0

font = pygame.font.Font(None, 36)


class Button:
    def __init__(self, text, position):
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.position = position
        self.rect = pygame.Rect(position, (200, 50))
        self.color = (100, 100, 100)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


start_stop_button = Button("Старт/Стоп", (50, SCREEN_HEIGHT - 100))
restart_button = Button("Начать с начала", (300, SCREEN_HEIGHT - 100))

allow_clicks = True  # Флаг для разрешения добавления нажатий кнопки мыши к счетчикам

def update_screen():
    screen.fill(color)
    screen.blit(target, (target_x, target_y))

    # Вывод количества успешных и неудачных попыток, попаданий и перемещений на экран
    successful_attempts_text = font.render(f"Успешных попыток: {successful_attempts}", True, (255, 255, 255))
    failed_attempts_text = font.render(f"Неудачных попыток: {failed_attempts}", True, (255, 255, 255))
    # hits_text = font.render(f"Попаданий: {successful_attempts}", True, (255, 255, 255))  # Убираем счетчик попаданий с экрана
    moves_text = font.render(f"Перемещений: {moves}", True, (255, 255, 255))
    screen.blit(successful_attempts_text, (10, 10))
    screen.blit(failed_attempts_text, (10, 50))
    # screen.blit(hits_text, (10, 90))  # Убираем счетчик попаданий с экрана
    screen.blit(moves_text, (10, 90))

    start_stop_button.draw()
    restart_button.draw()

    pygame.display.update()


# Функция для перемещения мишени
def move_target():
    global target_x, target_y, moves
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    moves += 1


running = True
paused = False
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, 2000)  # Генерация события каждую секунду

while running:
    update_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_stop_button.is_clicked(mouse_pos):
                if not paused:
                    allow_clicks = False
                paused = not paused
            elif restart_button.is_clicked(mouse_pos):
                total_attempts = 0
                successful_attempts = 0
                failed_attempts = 0
                moves = 0
                paused = False
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            elif not paused:
                total_attempts += 1
                if target_x < mouse_pos[0] < target_x + target_width and target_y < mouse_pos[1] < target_y + target_height:
                    successful_attempts += 1
                else:
                    failed_attempts += 1

        if event.type == move_event and not paused:  # Перемещение мишени по событию
            move_target()
            allow_clicks = True

pygame.quit()
