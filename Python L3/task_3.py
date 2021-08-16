# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(val_1, val_2, val_3):
    """Функция принимает три аргумента и возвращает сумму наибольших двух"""
    data = sorted([val_1, val_2, val_3])
    return f'{data[1]} + {data[2]} = {data[1] + data[2]}'


def ask_num():
    """Функция запрашивает ввод преобразует к типу float"""
    try:
        temp = input('Введите число - ')
        return float(temp)
    except ValueError:
        print(f'Ошибка: Ожидалось число, а получен тип {type(temp)}')
        return 0


def main():
    print(
        f'Сумма наибольших аргументов: {my_func(ask_num(), ask_num(), ask_num())}')


main()
