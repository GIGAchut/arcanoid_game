
def create_level(level, screen, Picture):
    # Параметры для расположения блоков
    block_width = 70
    block_height = 35

    num_rows = 4

    num_columns = 10

    x_offset = 50  # Начальный отступ от левого края
    y_offset = 70  # Начальный отступ от верхнего края
    horizontal_spacing = 10  # Горизонтальный промежуток между блоками
    vertical_spacing = 10  # Вертикальный промежуток между блоками
    # Вычисляем начальную позицию по X, чтобы блоки были выровнены по центру экрана
    start_x = (screen.get_width() - (num_columns * (block_width + horizontal_spacing) - horizontal_spacing)) // 2
    monsters = []
    # сплошная
    if level == 4:
        for row in range(num_rows):
            for col in range(num_columns):
                x = start_x + col * (block_width + horizontal_spacing)
                y = y_offset + row * (block_height + vertical_spacing)
                monsters.append(Picture(x, y, block_width, block_height))

    # шахматы
    if level == 3:
        for row in range(num_rows):
            for col in range(num_columns):
                if (row + col) % 2 == 0:
                    x = start_x + col * (block_width + horizontal_spacing)
                    y = y_offset + row * (block_height + vertical_spacing)
                    monsters.append(Picture(x, y, block_width, block_height))

    # узоры
    if level == 2:
        for row in range(num_rows):
            for col in range(num_columns):
                if row in [0, num_rows - 1] or col in [0, num_columns - 1]:
                    x = start_x + col * (block_width + horizontal_spacing)
                    y = y_offset + row * (block_height + vertical_spacing)
                    monsters.append(Picture(x, y, block_width, block_height))

    # диагональ
    if level == 1:
        for row in range(num_rows):
            for col in range(num_columns):
                if row == col or row + col == num_columns - 1:
                    x = start_x + col * (block_width + horizontal_spacing)
                    y = y_offset + row * (block_height + vertical_spacing)
                    monsters.append(Picture(x, y, block_width, block_height))


    return monsters