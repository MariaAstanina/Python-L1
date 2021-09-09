# Реализовать класс «Дата», функция - конструктор которого должна принимать дату в виде строки формата «день - месяц - год».
# В рамках класса реализовать два метода. Первый, с декоратором @ classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».Второй, с декоратором @ staticmethod, должен проводить валидацию
# числа, месяца и года(например, месяц — от 1 до 12).Проверить работу полученной структуры на реальных данных.
from dataclasses import dataclass


@dataclass
class Date:
    date: str

    @classmethod
    def my_int(cls, date):
        date_list = []
        try:
            date_list = [int(x) for x in date.split('-')]
        except ValueError:
            print("Ошибка в введенных данных")
        return date_list

    @staticmethod
    def check(date_list):
        days_in_month = {"январь": [1, 31], "февраль": [2, 29], "март": [3, 31], "апрель": [4, 30], "май": [5, 31],
                         "июнь": [6, 30], "июль": [7, 31], "августа": [8, 31], "сентябрь": [9, 30], "октябрь": [10, 31],
                         "ноябрь": [11, 30], "декабрь": [12, 31]}
        if len(date_list) == 3:
            if len([1 for el in days_in_month if
                    date_list[1] == days_in_month[el][0] and date_list[0] <= days_in_month[el][1]]) == 1 and date_list[
                2] < 2022 and date_list[2] > 1950:
                print('Данные введены корректно')
            else:
                print('Введенные данные не прошли валидацию')
        else:
            print('Неверный формат введенных данных')


Date.check(Date.my_int('31-12-2021'))
