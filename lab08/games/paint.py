import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x, y = 0, 0
    mode = 'blue'
    draw_mode = 'line'  # 'line', 'rect', 'circle', 'eraser'
    points = []

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Выбор цвета
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ увеличивает радиус
                    radius = min(50, radius + 2)
                elif event.button == 3:  # ПКМ уменьшает радиус
                    radius = max(5, radius - 2)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, draw_mode))
                points = points[-256:]  # Ограничение по точкам

        screen.fill((0, 0, 0))

        # Отрисовка элементов
        for i in range(len(points) - 1):
            drawTool(screen, i, points[i][0], points[i + 1][0], radius, mode, points[i][1])

        pygame.display.flip()
        clock.tick(60)

def drawTool(screen, index, start, end, width, color_mode, draw_mode):
    """Функция рисует линии, прямоугольники, круги и стирает"""
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)

    if draw_mode == 'line':
        pygame.draw.line(screen, color, start, end, width)
    elif draw_mode == 'rect':
        pygame.draw.rect(screen, color, (*start, width, width))
    elif draw_mode == 'circle':
        pygame.draw.circle(screen, color, start, width // 2)
    elif draw_mode == 'eraser':
        pygame.draw.circle(screen, (0, 0, 0), start, width)

main()