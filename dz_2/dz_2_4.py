# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количесво n элементов: '))
summ = 0
for i in range(n):
    summ += 1 / (-2) ** i
print(f'Сумма n элементов = {summ}')
