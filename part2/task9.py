# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" –
# соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 00.
# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3

string_text = 'ОООООООООО'
print(max(max(map(len, string_text.split('Р'))), max(map(len, string_text.split('О')))))





