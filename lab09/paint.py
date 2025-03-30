import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x, y = 0, 0
    mode = 'blue'
    draw_mode = 'line'  # line, rect, circle, eraser, square, rtriangle, etriangle, rhombus
    points = []

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (
                (event.key == pygame.K_w and ctrl_held) or
                (event.key == pygame.K_F4 and alt_held) or
                (event.key == pygame.K_ESCAPE))):
                return

            # Выбор цвета
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # Выбор инструмента
                if event.key == pygame.K_l:
                    draw_mode = 'line'
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_t:
                    draw_mode = 'rect'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'
                elif event.key == pygame.K_1:
                    draw_mode = 'square'
                elif event.key == pygame.K_2:
                    draw_mode = 'rtriangle'
                elif event.key == pygame.K_3:
                    draw_mode = 'etriangle'
                elif event.key == pygame.K_4:
                    draw_mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(50, radius + 2)
                elif event.button == 3:
                    radius = max(5, radius - 2)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, draw_mode))
                points = points[-256:]

        screen.fill((0, 0, 0))

        for i in range(len(points) - 1):
            drawTool(screen, i, points[i][0], points[i + 1][0], radius, mode, points[i][1])

        pygame.display.flip()
        clock.tick(60)

def drawTool(screen, index, start, end, width, color_mode, draw_mode):
    """Функция рисует различные фигуры"""
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    # Определение цвета
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)

    x1, y1 = start
    x2, y2 = end

    if draw_mode == 'line':
        pygame.draw.line(screen, color, start, end, width)
    elif draw_mode == 'rect':
        pygame.draw.rect(screen, color, (*start, width, width))
    elif draw_mode == 'circle':
        pygame.draw.circle(screen, color, start, width // 2)
    elif draw_mode == 'eraser':
        pygame.draw.circle(screen, (0, 0, 0), start, width)
    elif draw_mode == 'square':
        side = min(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(screen, color, (x1, y1, side, side), width=1)
    elif draw_mode == 'rtriangle':
        # Прямоугольный треугольник
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(screen, color, points, width=1)
    elif draw_mode == 'etriangle':
        # Равносторонний треугольник
        height = math.sqrt(3) / 2 * abs(x2 - x1)
        points = [
            ((x1 + x2) // 2, y1),  # верхняя вершина
            (x1, y1 + height),     # левая нижняя
            (x2, y1 + height)      # правая нижняя
        ]
        pygame.draw.polygon(screen, color, points, width=1)
    elif draw_mode == 'rhombus':
        # Ромб (4 точки: верх, правый, низ, левый)
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [
            (center_x, y1),       # верх
            (x2, center_y),       # право
            (center_x, y2),       # низ
            (x1, center_y)        # лево
        ]
        pygame.draw.polygon(screen, color, points, width=1)

main()