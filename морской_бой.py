# TODO: V - [ok]  [ok]  [ok]      H - [ok]  [ok]  [ok]
#           [ok]  [ok]  [ok]          [ok]  [ok]  [ok]
#           [ok]  [ok]  [ok]          [ok]  [ok]  [ok]

print('Если поля не появляются, PRESS RERUN')

import time
from random import *
pl_field = [['# ' for j in range(10)] for i in range(10)]
en_field = [['# ' for m in range(10)] for n in range(10)]

pl_ships_coord = []
en_ships_coord = []

show_enemy_field = input('Скрывать поле противника?(y/n)- ')
while show_enemy_field not in 'yn':
    show_enemy_field = input('Скрывать поле противника?(y/n)- ')

def draw_fields():

    # Поле пользователя
    print('  ', *[str(i)+' ' for i in range(1, 11)])  # рисуем цифры

    for i, j in zip(pl_field, 'ABCDEFGHIK'):  # рисуем буквы и поле боя
        print(j, '', *i)

    print()

    # Поле противника (его я специально не рисую, т.к. по правилам поле противника не должно быть видно)
    if show_enemy_field == 'n':
        print('  ', *[str(i) + ' ' for i in range(1, 11)])   # рисуем цифры

        for i, j in zip(en_field, 'ABCDEFGHIK'):  # рисуем буквы и поле боя
            print(j, '', *i)


def draw_ships(rows: list, col: int, orient: str, field: list):

    if orient == 'V':
        # Рисую корабль
        for ind in range(len(field)):
            if ind in rows:
                field[ind][col] = '@ '

        # рисуем границы [V-корабля]
        # -----------------
        if rows[0] == 0 and col != 9 and col != 0:
            for row_ind in rows:
                field[row_ind][col + 1], field[row_ind][col - 1] = '. ', '. '
            field[rows[-1] + 1][col], field[rows[-1] + 1][col + 1], field[rows[-1] + 1][col - 1] = '. ', '. ', '. '

        elif rows[0] == 0 and col == 0:
            for row_ind in rows:
                field[row_ind][col + 1] = '. '
            field[rows[-1] + 1][col], field[rows[-1] + 1][col + 1] = '. ', '. '

        elif rows[0] == 0 and col == 9:
            for row_ind in rows:
                field[row_ind][col - 1] = '. '
            field[rows[-1] + 1][col], field[rows[-1] + 1][col - 1] = '. ', '. '
        # --------------------
        elif (rows[0] != 0 and rows[-1] != 9) and col != 0 and col != 9:
            for row_ind in rows:
                field[row_ind][col + 1], field[row_ind][col - 1] = '. ', '. '
            field[rows[-1] + 1][col], field[rows[-1] + 1][col - 1], field[rows[-1] + 1][col + 1] = '. ', '. ', '. '
            field[rows[0] - 1][col], field[rows[0] - 1][col - 1], field[rows[0] - 1][col + 1] = '. ', '. ', '. '

        elif (rows[0] != 0 and rows[-1] != 9) and col == 0:
            for row_ind in rows:
                field[row_ind][col + 1] = '. '
            field[rows[-1] + 1][col], field[rows[-1] + 1][col + 1] = '. ', '. '
            field[rows[0] - 1][col], field[rows[0] - 1][col + 1] = '. ', '. '

        elif (rows[0] != 0 and rows[-1] != 9) and col == 9:
            for row_ind in rows:
                field[row_ind][col - 1] = '. '
            field[rows[-1] + 1][col], field[rows[-1] + 1][col - 1] = '. ', '. '
            field[rows[0] - 1][col], field[rows[0] - 1][col - 1] = '. ', '. '
        # --------------------
        elif rows[-1] == 9 and col != 0 and col != 9:
            for row_ind in rows:
                field[row_ind][col + 1], field[row_ind][col - 1] = '. ', '. '
            field[rows[0] - 1][col], field[rows[0] - 1][col + 1], field[rows[0] - 1][col - 1] = '. ', '. ', '. '

        elif rows[-1] == 9 and col == 0:
            for row_ind in rows:
                field[row_ind][col + 1] = '. '
            field[rows[0] - 1][col], field[rows[0] - 1][col + 1], = '. ', '. '

        elif rows[-1] == 9 and col == 9:
            for row_ind in rows:
                field[row_ind][col - 1] = '. '
            field[rows[0] - 1][col], field[rows[0] - 1][col - 1], = '. ', '. '

    elif orient == 'H':
        # cols ~ rows; row ~ col
        cols, row = rows, col

        # Рисует корабль
        for ind in range(len(field)):
            if ind in cols:
                field[row][ind] = '@ '

        # рисует границы [H-корабля]
        # -----------------
        if row == 0 and cols[0] != 0 and cols[-1] != 9:
            for col_ind in cols:
                field[row+1][col_ind] = '. '
            field[row][cols[0]-1], field[row][cols[-1]+1],\
            field[row+1][cols[0]-1], field[row+1][cols[-1]+1] = '. ', '. ', '. ', '. '

        elif row == 0 and cols[0] == 0:
            for col_ind in cols:
                field[row + 1][col_ind] = '. '
            field[row+1][cols[-1]+1], field[row][cols[-1]+1] = '. ', '. '

        elif row == 0 and cols[-1] == 9:
            for col_ind in cols:
                field[row+1][col_ind] = '. '
            field[row+1][cols[0]-1], field[row][cols[0]-1] = '. ', '. '
        # --------------------
        elif (row != 0 and row != 9) and (cols[0] != 0 and cols[-1] != 9):
            for col_ind in cols:
                field[row-1][col_ind], field[row+1][col_ind] = '. ', '. '
            field[row-1][cols[0]-1], field[row-1][cols[-1]+1], field[row][cols[0]-1], field[row][cols[-1]+1],\
            field[row+1][cols[0]-1], field[row+1][cols[-1]+1] = '. ', '. ', '. ', '. ', '. ', '. '

        elif (row != 0 and row != 9) and cols[0] == 0:
            for col_ind in cols:
                field[row-1][col_ind], field[row+1][col_ind] = '. ', '. '
            field[row][cols[-1]+1], field[row+1][cols[-1]+1], field[row-1][cols[-1]+1] = '. ', '. ', '. '

        elif (row != 0 and row != 9) and cols[-1] == 9:
            for col_ind in cols:
                field[row-1][col_ind], field[row+1][col_ind] = '. ', '. '
            field[row][cols[0] - 1], field[row + 1][cols[0] - 1], field[row - 1][cols[0] - 1] = '. ', '. ', '. '
        # -----------------
        elif row == 9 and cols[0] != 0 and cols[-1] != 9:
            for col_ind in cols:
                field[row-1][col_ind] = '. '
            field[row][cols[0]-1], field[row][cols[-1]+1], field[row-1][cols[0]-1],\
            field[row-1][cols[-1]+1] = '. ', '. ', '. ', '. '

        elif row == 9 and cols[0] == 0:
            for col_ind in cols:
                field[row-1][col_ind] = '. '
            field[row][cols[-1]+1], field[row-1][cols[-1]+1] = '. ', '. '

        elif row == 9 and cols[-1] == 9:
            for col_ind in cols:
                field[row-1][col_ind] = '. '
            field[row][cols[0]-1], field[row-1][cols[0]-1] = '. ', '. '



def set_ships_position(field: list, ships_coord: list):

    ship_orient = [choice(['V', 'H']) for i in range(5)]  # массив с 5-ю ориентациями для кораблей
    ships_length = [4, 3, 3, 2, 2]  # Виды кораблей

    for i in range(len(ship_orient)):

        if ship_orient[i] == 'V':  # Код создает координаты одного [V-корабля] и рисует его на поле

            col = randint(0, 9)  # Нужен 1 индекс столбца
            rows = []  # Нужны индексы рядов

            while 1:

                for ln in range(ships_length[i]):
                    # Код отвечает за то, чтобы координаты не повторялись
                    pos = randint(0, 9)
                    while pos in rows:
                        pos = randint(0, 9)
                    rows.append(pos)

                # Если разность любых соседних чисел не равно 1, то корабль нарисуется некорректно
                alright = 0
                for k in range(len(rows)-1):
                    if abs(rows[k]-rows[k+1]) != 1:  # Проверка на правильность позиций корабля
                        rows.clear()
                        break
                    else:
                        alright += 1


                if alright == len(rows)-1:  # Значит координаты корабля нас устраивают и можем выйти из цикла

                    # Можно ли рисовать в данных координатах корабль
                    flag = True
                    for index in rows:
                        if field[index][col] == '@ ' or field[index][col] == '. ':
                            rows.clear()
                            flag = False

                    if not flag:  # Я завел этот флаг для того чтобы continue действовал на объемлюющий цикл while
                        continue


                    break  # Иначе меня всё устраивает: координаты выбраны правильно, на данных координатах не нарисован другой корабль

            rows = sorted(rows)

            ships_coord.append(('V', col, rows))

            draw_ships(rows, col, 'V', field)  # вызываю функцию для отрисовки кораблей внутри другой

        # ----------------------

        elif ship_orient[i] == 'H':  # Код создает координаты одного [H-корабля] и рисует его на поле

            cols = []  # Нужны индексы столбцов
            row = randint(0, 9)  # Нужен 1 индекс ряда

            while 1:

                for ln in range(ships_length[i]):
                    # Код отвечает за то, чтобы координаты не повторялись
                    pos = randint(0, 9)
                    while pos in cols:
                        pos = randint(0, 9)
                    cols.append(pos)

                # Если разность любых соседних чисел не равно 1, то корабль нарисуется некорректно
                alright = 0
                for k in range(len(cols)-1):
                    if abs(cols[k]-cols[k+1]) != 1:  # Проверка на правильность позиций корабля
                        cols.clear()
                        break
                    else:
                        alright += 1

                if alright == len(cols)-1:  # Значит координаты корабля нас устраивают и можем выйти из цикла

                    # Можно ли рисовать в данных координатах корабль
                    flag = True
                    for index in cols:
                        if field[row][index] == '@ ' or field[row][index] == '. ':
                            cols.clear()
                            flag = False

                    if not flag:  # Я завел этот флаг для того чтобы continue действовал на объемлюющий цикл while
                        continue


                    break  # Иначе меня всё устраивает: координаты выбраны правильно, на данных координатах не нарисован другой корабль

            cols = sorted(cols)

            ships_coord.append(('H', row, cols))

            draw_ships(cols, row, 'H', field)  # вызываю функцию для отрисовки кораблей внутри другой


def pl_whoop(enem_field: list, func_name, ships_coords: list, name: str):  # пли! (игрок)

    d_guess = {i:j for i, j in zip('ABCDEFGHIK', range(0, 10))}  # словарь, где ключи - это буквы слева от поля,
    # а значения - индекс вложенных массивов
    d_numbers = {i: j for i, j in zip(f'123456789', range(0, 9))}  # словарь, где - ключи цифры вверху поля, а
    # значения - индексы символов вложенных массивов
    d_numbers['10'] = 9

    print('Твой ход!')
    coord_choose = input('Введи координаты для удара(напр.- A1): ')

    while enem_field[d_guess[coord_choose[0].upper()]][d_numbers[coord_choose[1:]]] == '@ ':
        print('Попадание!')

        enem_field[d_guess[coord_choose[0].upper()]][d_numbers[coord_choose[1:]]] = 'K '  # область корабля уничтожается(@ --> K)

        res = func_name(en_field, ships_coords, name)
        if res != None:
            print(res)

        time.sleep(1)
        print('Твой ход!')

        coord_choose = input('Введи координаты для удара: ')

    print('Промах..')
    enem_field[d_guess[coord_choose[0].upper()]][d_numbers[coord_choose[1:]]] = 'm '
    time.sleep(1)


def en_whoop(player_field: list, func_name, ships_coords: list, name: str):  # пли! (противник)

    d_guess = {str(i): j for i, j in zip(range(0, 10), 'ABCDEFGHIK')}
    d_numbers = {str(i): j for i, j in zip(range(0, 9), f'123456789')}
    d_numbers['9'] = '10'

    coord_choose = str(randint(0, 10))+str(randint(0, 10))

    print(f'Ход противника! - {d_guess[coord_choose[0]]+d_numbers[coord_choose[1]]}')
    time.sleep(1)

    while player_field[int(coord_choose[0])][int(coord_choose[1])] == '@ ':

        player_field[int(coord_choose[0])][int(coord_choose[1])] = 'K '  # область корабля уничтожается(# --> K)
        print('Попадание!')

        res = func_name(player_field, ships_coords, name)
        if res != None:
            print(res)

        time.sleep(1)

        coord_choose = str(randint(0, 10)) + str(randint(0, 10))

        print(f'Ход противника! - {d_guess[coord_choose[0]] + d_numbers[coord_choose[1]]}')
        time.sleep(1)

    print('Промах!')
    time.sleep(1)

    player_field[int(coord_choose[0])][int(coord_choose[1])] = 'm '


def check_destroy_ship(field: list, ships_coords: list, name: str) -> str:  # функция для вывода сообщения, что корабль
    # уничтожен

    for tpl_ind in range(len(ships_coords)):

        if ships_coords[tpl_ind][0] == 'V':

            hits = 0

            for i in range(len(field)):  # ОПТИМИЗИРОВАТЬ(DRY)
                for j in range(len(field[i])):
                    if i in ships_coords[tpl_ind][2] and j == ships_coords[tpl_ind][1] and field[i][j] == 'K ':
                        hits += 1

            if len(ships_coords[tpl_ind][2]) == hits:
                ships_coords.remove(ships_coords[tpl_ind])
                return f'Корабль {name}а уничтожен!'

        elif ships_coords[tpl_ind][0] == 'H':

            hits = 0

            for i in range(len(field)):
                for j in range(len(field[i])):
                    if j in ships_coords[tpl_ind][2] and i == ships_coords[tpl_ind][1] and field[i][j] == 'K ':
                        hits += 1

            if len(ships_coords[tpl_ind][2]) == hits:
                del ships_coords[tpl_ind]
                return f'Корабль {name}а уничтожен!'



def check_winner(field1, field2, name1, name2):
    global flag

    count_1 = sum([1 for i in field1 for j in i if j == '@ '])
    count_2 = sum([1 for i in field2 for j in i if j == '@ '])

    if count_1 == 0:
        print(f'Победитель: {name2}')
        flag = 0

    if count_2 == 0:
        print(f'Победитель: {name1}')
        flag = 0


# def clear_borders(field):  # Очищает границы кораблей(точки), т.е скрывает границы кораблей
#     for i in range(len(field)):
#         for j in range(len(field[i])):
#             if field[i][j] == '. ':
#                 field[i][j] = '# '

set_ships_position(pl_field, pl_ships_coord)
set_ships_position(en_field, en_ships_coord)

# clear_borders(pl_field)
# clear_borders(en_field)

flag = 1

while flag:

    draw_fields()

    pl_whoop(en_field, check_destroy_ship, en_ships_coord, 'противник')

    en_whoop(pl_field, check_destroy_ship, pl_ships_coord, 'игрок')

    check_winner(pl_field, en_field, 'Ты', 'противник')