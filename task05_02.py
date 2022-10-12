# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# =====================================================================
#
#
# Игра компьютер против человека.
# Вроде получилось если компьютер ходит первым, то всегда выигрывает
# Компьтер выигрывает у человека, и играя вторым, если тот ошибется
# Возможность загадывать размер куша от 70 до 3000 (можно менять)
# Возможность загадывать размер хода от 7 до 70 (можно менять)
# Можно было поиграться с поддавками компьютера, но не укладываюсь в сроки
#
#
# ======================================================================

import random


def get_random_true_false(num):
    first_second = random.randint(1, num)
    if first_second % 2 == 0:
        print('Игру начинает компьютер')
        return True
    else:
        print('Игру начинаете Вы')
        return False


def get_int_number(str_1, num_min, num_max):
    while True:
        try:
            num = int(input(str_1))
            if num_max >= num >= num_min:
                return num
            else:
                print(
                    f'Введенное число меньше {num_min} или больше {num_max}. Повторите ввод')
        except ValueError:
            print("Вы ввели не натуральное число. Повторите ввод")


def get_game(flag, total, step):
    flag01 = True
    # balance = 0
    while total > 0:
        if flag:
            if flag01:
                balance = (total % (step + 1))
                if balance == 0:
                    balance = step
                flag01 = False
            else:
                balance = step + 1 - user
            total -= balance
            print(f'Компьютер сделал ход: {balance}')
            print('Осталось конфет: ' + str(total))
            if total <= 0:
                print('Компьютер выиграл!!!')
                return
            flag = False
        else:
            user = get_int_number(
                'Сколько конфет хотите взять?: ', 1, user_step)
            total -= user
            balance = total % (step + 1)
            if not balance == 0:
                flag01 = True
            else:
                flag01 = False
            print('Осталось конфет: ' + str(total))
            if total <= 0:
                print('Вы выиграли!!!')
                return
            flag = True


size_jackpot = get_int_number(
    'Сколько разыгрываем конфет (от 70 до 3000)?: ', 70, 3000)
user_step = get_int_number('Сколько будем брать за раз (от 7 до 70)?: ', 7, 70)
user_flag = get_random_true_false(100)
get_game(user_flag, size_jackpot, user_step)
