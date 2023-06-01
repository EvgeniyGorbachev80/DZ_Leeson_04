# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
#            причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
#            Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
#            на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве 
#            внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
#            собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
#            собирает ягоды с этого куста и с двух соседних с ним.
#            Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
#            находясь перед некоторым кустом заданной во входном файле грядки.

#            Например: 4 -> 1 2 3 4
#                      9


n = 5 # кустов
from random import randint
list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
    res = list_1[-2] + list_1[-1] + list_1[0]
else:
    res = list_1[a-1] + list_1[a-2] + list_1[a]
print(res, 'ягод')



# Пример идеального решения

# n = int(input())
# arr = list()
# for i in range(n):
#     x = int(input())
#     arr.append(x)

# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))