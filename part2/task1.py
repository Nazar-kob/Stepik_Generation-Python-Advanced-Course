# Координатные четверти
# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
# Формат входных данных
# В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел —
# координат точки (сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.
# Формат выходных данных
# Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.
# Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.
# Тестовые данные 🟢
# Sample Input 1:
# 4
# 0 -1
# 1 2
# 0 9
# -9 -5
# Sample Output 1:
# Первая четверть: 1
# Вторая четверть: 0
# Третья четверть: 1
# Четвертая четверть: 0




def find_coord(x: list) -> dict:
    parts = {'Первая четверть:': 0, 'Вторая четверть:': 0, 'Третья четверть:': 0, 'Четвертая четверть:': 0}
    for i in x:
        if i[0] > 0 and i[1] > 0:
            parts['Первая четверть:'] += 1
        elif i[0] < 0 and i[1] > 0:
            parts['Вторая четверть:'] += 1
        elif i[0] < 0 and i[1] < 0:
            parts['Третья четверть:'] += 1
        elif i[0] > 0 and i[1] < 0:
            parts['Четвертая четверть:'] += 1
    return parts


def add_coordinates(amount: int) -> list:
    list_coordinates = []
    for i in range(amount):
        x, y = map(int, input().split())
        list_coordinates.append((x, y))
    return list_coordinates


def task1():
    x = add_coordinates(int(input()))
    y = find_coord(x)
    for x, y in y.items():
        print(x, y)


if __name__ == '__main__':
    task1()
