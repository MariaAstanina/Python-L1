# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки: ручка')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки: карандаш')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки: маркер')


pen = Pen().draw()
pencil = Pencil().draw()
handle = Handle().draw()

