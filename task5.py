# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.
def reserve_number(n):
    reserved_number=0
    while n>0:
        last = n % 10
        reserved_number = reserved_number*10 + last
        n//=10
    return  reserved_number
n = int(input())
print(reserve_number(n))

