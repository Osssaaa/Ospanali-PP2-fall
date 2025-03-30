import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

BACKGROUND = (245, 222, 179)
GRID_LIGHT = (255, 165, 79)
GRID_DARK = (255, 140, 0)
SNAKE_COLOR = (0, 100, 0)
FOOD_COLOR = (220, 20, 60)
TEXT_COLOR = (139, 69, 19)
GAME_OVER_BG = (255, 69, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_grid(surface):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = GRID_LIGHT if (x + y) % 2 == 0 else GRID_DARK
            pygame.draw.rect(surface, color, rect)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = SNAKE_COLOR

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point

    def move(self):
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_pos = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)

        if new_pos[0] < 0 or new_pos[0] >= WIDTH or new_pos[1] < 0 or new_pos[1] >= HEIGHT:
            return False

        if new_pos in self.positions:
            return False

        self.positions.insert(0, new_pos)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def grow(self, amount):
        self.length += amount

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, GRID_LIGHT, rect, 1)

class Food:
    def __init__(self, snake_positions):
        self.color = FOOD_COLOR
        self.randomize_position(snake_positions)
        self.weight = random.randint(1, 3)  # Вес еды (насколько змейка увеличится)
        self.timer = random.randint(5, 10) * 1000  # Время исчезновения еды (мс)
        self.spawn_time = pygame.time.get_ticks()

    def randomize_position(self, snake_positions):
        while True:
            new_pos = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                       random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            if new_pos not in snake_positions:
                self.position = new_pos
                self.spawn_time = pygame.time.get_ticks()
                break

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.timer

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, GRID_LIGHT, rect, 1)

def show_text(surface, text, size, x, y):
    font = pygame.font.SysFont("monospace", size)
    label = font.render(text, True, TEXT_COLOR)
    surface.blit(label, (x, y))

def main():
    snake = Snake()
    food = Food(snake.positions)
    running = True
    score = 0
    level = 1
    speed = 5

    while running:
        screen.fill(BACKGROUND)
        draw_grid(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        if not snake.move():
            break

        if snake.get_head_position() == food.position:
            snake.grow(food.weight)
            score += food.weight
            food.randomize_position(snake.positions)

            if score % 5 == 0:
                level += 1
                speed += 1

        if food.is_expired():
            food.randomize_position(snake.positions)

        snake.draw(screen)
        food.draw(screen)
        show_text(screen, f"Score: {score}", 20, 10, 10)
        show_text(screen, f"Level: {level}", 20, 500, 10)

        pygame.display.flip()
        clock.tick(speed)

    screen.fill(GAME_OVER_BG)
    show_text(screen, "GAME OVER", 50, WIDTH // 2 - 100, HEIGHT // 2 - 25)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()