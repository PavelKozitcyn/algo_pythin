# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('n - любое натуральное число: '))
summ = 0
for i in range(1, n + 1):
    summ += i
if summ == n * (n + 1) / 2:
    print('Выражение верно')
else:
    print('Выражение неверно')