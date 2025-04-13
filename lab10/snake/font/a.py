import pygame
import random
import psycopg2
from config import load_config


def query(name):
    sql = 'SELECT * FROM usernames WHERE Name = %s'

    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (name,))
                rows = cursor.fetchall()
                return rows  # Возвращаем список строк
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при запросе:", error)
        return []  # Возвращаем пустой список в случае ошибки



def insert_data(name):
    sql = """INSERT INTO usernames(Name, Score, Level, Length, FPS)
             VALUES (%s, %s, %s, %s, %s)
             ON CONFLICT (Name) DO NOTHING;"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (name, 0, 1, 2, 5))
                connection.commit()
                print("Данные успешно добавлены.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при вставке:", error)

def update_player_data(name, score, level, length, fps):
    sql = """UPDATE usernames
             SET Score = %s, Level = %s, Length = %s, FPS = %s
             WHERE Name = %s;"""

    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (score, level, length, fps, name))
                connection.commit()
                print("Данные игрока обновлены.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при обновлении:", error)


def add_new_player(name):
    sql = """INSERT INTO usernames (Name, Level, Score, Length, FPS)
             VALUES (%s, 0, 0, 1, 5);"""  # Начальные значения: level=0, score=0, length=1

    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (name,))
                connection.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при добавлении игрока:", error)



def run_snake_game(username):
    data = query(username)
    
    # Убедимся, что данные получены
    if not data:
            print(f"Игрок {username} не найден в базе данных. Создаем нового игрока...")
            add_new_player(username)
            data = query(username)

    # Доступ к данным игрока
    name, level, score, length, fps = data[0]

    if fps is None:
        fps = 5

    pygame.init()
    cell_size = 40
    cell_number = 20
    screen_width = cell_size * cell_number
    screen_height = cell_size * cell_number
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font("font/Pixeltype.ttf", 50)

    color_red = (255, 0, 0)
    color_purple = (128, 0, 128)
    color_orange = (255, 68, 51)
    color_green = (0, 255, 0)
    color_white = (255, 255, 255)

    x_pos = 0
    y_pos = 0
    direction = "UP"

    x_ch = (cell_number // 2) * cell_size
    y_ch = (cell_number // 2) * cell_size
    snake_lst = [[x_ch, y_ch]]
    length = length  # Теперь это число длины змейки, полученное из базы данных

    x_f = 0
    y_f = 0
    fruit_types = [(color_red, 1), (color_purple, 2), (color_orange, 3)]
    fruit_spawn_time = 5000
    last_fruit_time = pygame.time.get_ticks()
    fruit_info = (color_red, 1)

    done = False
    score = score  # Текущий счет игрока
    level = level  # Текущий уровень игрока
    fps = fps

    def game_over(x, y, snake_list):
        return x < 0 or x >= screen_width or y < 0 or y >= screen_height or [x, y] in snake_list[:-1]

    def generate_fruit(snake_list, current_level):
        while True:
            x = random.randint(0, cell_number - 1) * cell_size
            y = random.randint(0, cell_number - 1) * cell_size
            if [x, y] not in snake_list:
                if current_level < 3:
                    return x, y, (color_red, 1)
                return x, y, random.choice(fruit_types)

    x_f, y_f, fruit_info = generate_fruit(snake_lst, level)

    def draw_snake(snake_list, color, surface, cell_size):
        for segment in snake_list:
            pygame.draw.rect(surface, color, (segment[0], segment[1], cell_size, cell_size))

    while not done:
        pygame.display.set_caption(f"Score: {score} Level: {level}")
        screen.fill(color_white)

        current_time = pygame.time.get_ticks()
        if current_time - last_fruit_time >= fruit_spawn_time:
            x_f, y_f, fruit_info = generate_fruit(snake_lst, level)
            last_fruit_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_player_data(username, score, level, length, fps)
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    update_player_data(username, score, level, length, fps)
                    return
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"

        if direction == "UP":
            y_pos = -cell_size
            x_pos = 0
        elif direction == "DOWN":
            y_pos = cell_size
            x_pos = 0
        elif direction == "RIGHT":
            x_pos = cell_size
            y_pos = 0
        elif direction == "LEFT":
            x_pos = -cell_size
            y_pos = 0

        x_ch += x_pos
        y_ch += y_pos

        if game_over(x_ch, y_ch, snake_lst):
            screen.fill(color_white)
            message = font.render("GAME OVER", True, color_red)
            message_rect = message.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(message, message_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            update_player_data(username, 0, 0, 2, 5)
            return

        snake_lst.append([x_ch, y_ch])
        if len(snake_lst) > length:
            del snake_lst[0]

        if x_ch == x_f and y_ch == y_f:
            last_fruit_time = current_time
            score += fruit_info[1]
            length += fruit_info[1]
            x_f, y_f, fruit_info = generate_fruit(snake_lst, level)

        if score >= 5:
            score = 0
            level += 1
            fps += 3

        pygame.draw.rect(screen, fruit_info[0], (x_f, y_f, cell_size, cell_size))
        draw_snake(snake_lst, color_green, screen, cell_size)

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    cell_size = 40
    cell_number = 20
    screen_width = cell_size * cell_number
    screen_height = cell_size * cell_number
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.Font("font/Pixeltype.ttf", 50)
    user_font = pygame.font.Font(None, 25)
    user_text = ''
    username_rect = pygame.Rect(330, 300, 150, 32)
    text = font.render("PRESS ENTER TO START", True, 'Red')
    color_white = (255, 255, 255)

    while True:
        done = False
        while not done:
            screen.fill(color_white)
            text_surface = user_font.render(user_text, True, (0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        insert_data(user_text)
                        run_snake_game(user_text)
                        user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

            pygame.draw.rect(screen, (0, 255, 0), username_rect, 3)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
            screen.blit(text_surface, (username_rect.x + 5, username_rect.y + 5))
            username_rect.w = max(100, text_surface.get_width() + 10)
            pygame.display.flip()