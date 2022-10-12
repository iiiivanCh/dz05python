# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

given_str = 'ayjpабв ykабвu [poooабвoo bmuo[[[[[[а бв[[u,opiibu[ poабв,u]] sdfdsf given user rtyy rtyабв'
result = ''
user_list = given_str.split(' ')
for i in user_list:
    if 'абв' not in i:
        result += i + ' '
print(result)
