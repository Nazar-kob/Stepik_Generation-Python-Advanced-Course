# task 1
def find_coord(x: list) -> dict:
    parts = {'Первая четверть:': 0, 'Вторая четверть:': 0, 'Третья четверть:': 0, 'Четвертая четверть:': 0}
    for i in x:
        if i[0] >= 0 and i[1] >= 0:
            parts['Первая четверть:'] += parts['Первая четверть:'] + 1
            print(f'Первая четверть:{i[0], i[1]}')
        elif i[0] <= 0 and i[1] >= 0:
            parts['Вторая четверть:'] += parts['Вторая четверть:'] + 1
            print(f'Вторая четверть:{i[0], i[1]}')
        elif i[0] <= 0 and i[1] <= 0:
            parts['Третья четверть:'] += parts['Третья четверть:'] + 1
            print(f'Третья четверть:{i[0], i[1]}')
        elif i[0] >= 0 and i[1] <= 0:
            parts['Четвертая четверть:'] += parts['Четвертая четверть:'] + 1
            print(f'Четвертая четверть:{i[0], i[1]}')
    return parts


def add_coordinates(amount: int) -> list:
    list_coordinates = []
    for i in range(amount):
        x, y = map(int, input().split())
        list_coordinates.append((x, y))
    return list_coordinates

x = add_coordinates(int(input()))
y = find_coord(x)
for x, y in y.items():
    print(x, y)