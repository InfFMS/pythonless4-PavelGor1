# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def rasklad(n, divisor=2):
    if n == 1:
        return []
    # Если текущий делитель делит n нацело, добавляем его в список
    if n % divisor == 0:
        return [divisor] + rasklad(n // divisor, divisor)
    else:
        # Если делитель не подходит, увеличиваем делитель и продолжаем
        return rasklad(n, divisor + 1)


def format(n):
    factors = rasklad(n)
    return '*'.join(map(str, factors))
number = int(input())
result = format(number)
print(result)