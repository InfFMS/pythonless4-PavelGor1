# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def f(chislitel,znamenatel):
    chislitel_delitel = 0
    znamenatel_delitel = 0
    ans1= 0
    ans2=0
    ans3 = 0
    ans4 = 0
    if chislitel > znamenatel:
        for i in range(1,chislitel):
            if chislitel% i ==0:
                chislitel_delitel = i
            if znamenatel % chislitel_delitel == 0:
                ans1 = chislitel//chislitel_delitel
                ans2 = znamenatel//chislitel_delitel
    print(ans1,ans2)

    if znamenatel > chislitel:
        for j in range(1,znamenatel):
            if znamenatel% j ==0:
                znamenatel_delitel = j
            if chislitel % znamenatel_delitel == 0:
                ans3 = chislitel // znamenatel_delitel
                ans4 = znamenatel // znamenatel_delitel
    print(ans3,ans4)
    if znamenatel == chislitel:
        print(chislitel,znamenatel)
a,b=map(int,input().split())
print(f(a,b))
