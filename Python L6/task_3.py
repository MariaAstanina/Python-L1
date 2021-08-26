# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
   
    @property
    def income(self):
        return self._income

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": 0, "bonus": 0}
        for num, st in enumerate(self.income):
            self.income[st] = income[num]


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Доход сотрудника - {self.income["wage"] + self.income["bonus"]}')


Art = Position('Artem', 'Shulin', 'Analist', [125_000, 10_000])
print(f'имя:{Art.name}  фамилия:{Art.surname}  должность:{Art.position}  оклад:{Art.income["wage"]}  премия:{Art.income["bonus"]}')
Art.get_full_name()
Art.get_total_income()
