# Lesson_OG03
![Logo](F:\GitHub\Lesson_OG03\Img_lib\target.jpg)
# Игра Тир

Игра Тир представляет собой простую игру, в которой игрок должен попадать в мишень, используя мышь. Вот описание основных функций игры:

## Основные функции

### 1. update_screen()

   - Функция обновляет экран игры, отображая текущее состояние игры, включая количество успешных и неудачных попыток, количество перемещений мишени и т. д.

### 2. move_target()

   - Функция перемещает мишень по экрану, задавая случайные координаты.

### 3. Button

   - Класс кнопки представляет собой кнопку управления игрой. Кнопки включают "Старт/Стоп" и "Начать с начала".

### 4. pygame.event.get()

   - Обработка событий, таких как нажатие клавиш и перемещение мыши, для взаимодействия с игрой.

### 5. Глобальные переменные

   - В игре есть ряд глобальных переменных, таких как `total_attempts`, `successful_attempts`, `failed_attempts`, `moves`, которые отслеживают состояние игры и статистику.

## Запуск игры

Для запуска игры выполните следующие действия:

1. Запустите скрипт `main.py`.
2. Используйте мышь для взаимодействия с игрой.
3. Нажмите кнопку "Старт/Стоп", чтобы начать или приостановить игру.
4. Нажмите кнопку "Начать с начала", чтобы начать игру заново.

## Требования

- Python 3.x
- Pygame
