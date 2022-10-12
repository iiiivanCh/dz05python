# Создайте программу для игры в ""Крестики-нолики""


import random


def get_print_boards():
    print(boards[0], end=' ')
    print(boards[1], end=' ')
    print(boards[2])
    print(boards[3], end=' ')
    print(boards[4], end=' ')
    print(boards[5])
    print(boards[6], end=' ')
    print(boards[7], end=' ')
    print(boards[8])


def get_random_true_false(num):
    first_second = random.randint(1, num)
    if first_second % 2 == 0:
        print('Игру игрок 1')
        return True
    else:
        print('Игру игрок 2')
        return False


def get_step_boards(step, mark):
    i = boards.index(step)
    boards[i] = mark


def get_result():
    p = ''
    for i in victories:
        if boards[i[0]] == 'X' and boards[i[1]] == 'X' and boards[i[2]] == 'X':
            p = 'X'
        if boards[i[0]] == 'O' and boards[i[1]] == 'O' and boards[i[2]] == 'O':
            p = 'O'
    return p


def get_game():
    game_over = False
    flag = get_random_true_false(100)
    while game_over == False:
        get_print_boards()
        if flag == True:
            sign = 'X'
            step = int(input('Игрок 1, ваш ход: '))
        else:
            sign = 'O'
            step = int(input('Игрок 2, ваш ход: '))
        get_step_boards(step, sign)
        v = get_result()
        if v != '':
            game_over = True
        else:
            game_over = False
        flag = not (flag)
    get_print_boards()
    if v == 'X':
        print('Победил игрок 1')
    else:
        print('Победил игрок 2')


boards = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


get_game()
