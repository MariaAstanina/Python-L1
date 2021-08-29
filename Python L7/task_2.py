# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure


class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def expenditure(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def expenditure(self):
        return 2 * self.height + 0.3


coat = Coat('Пальто', 10)
suit = Suit('Костюм', 10)
print(f'Расход ткани на пошив {coat.name} - {coat.expenditure}')
print(f'Расход ткани на пошив {suit.name} - {suit.expenditure}')
print(coat + suit)
