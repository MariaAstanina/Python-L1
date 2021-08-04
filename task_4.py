# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число - '))
max_dg = number % 10
while number >= 10:
    number = number // 10
    last_dg = number % 10
    if max_dg < last_dg:
        max_dg = last_dg

print(max_dg)
