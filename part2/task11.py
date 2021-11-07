# Роскомнадзор запретил букву а 🌶️🌶️
# Необходимо написать программу, реализующую алгоритм написания этой песни.
# Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
# если она встречается в строке текста, а очередную строку отображает уже без этой буквы.
# Формат входных данных
# На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".
# Формат выходных данных
# Программа должна вывести в соответствии с указанным алгоритмом строки,
# количество которых равно количеству разных букв в строке,
# которая получается путем конкатенации введенного слова и строки "запретил букву".
# Примечание 1. Текст исходной песни в первом тесте.
# Примечание 2. Поем и решаем, друзья, поем и решаем 😂.


alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = input() + ' запретил букву'

for letter in alphabet:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()
        if word == '':
            break