# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
def is_number(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


# Почему list, а не tuple
seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
users_month = input('Введите номер месяца -')
if is_number(users_month):
    users_month_int = int(users_month)
    if users_month_int >= 1 and users_month_int <= 12:
        for el in seasons:
            if users_month_int in seasons[el]:
                print(f'{users_month}-ый месяц в году - {el}')
                break
    else:
        print('Введенное Вами число не соответсвует номеру месяца')

else:
    print('Вы ввели не число')
