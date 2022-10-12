# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def get_coding(text):
    with open(text, 'r') as data:
        txt = data.readline()
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
        with open('coding.txt', 'w') as data:
            data.write(res)


def get_decoding(text):
    with open(text, 'r') as data:
        txt = data.readline()
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    with open('decoding.txt', 'w') as data:
        data.write(res)
    return res


get_coding('text.txt')
get_decoding('coding.txt')
