# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорось автомобиля {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорось автомобиля {self.name} - {self.speed} км/ч') if self.speed <= 60 else print(
            f'Автомобиль {self.name} превысил скорость на {self.speed - 60} км/ч')


class SportCar(Car):
    min_speed = 190

    def show_speed(self):
        print(f'Текущая скорось автомобиля {self.speed} км/ч') if self.speed >= self.min_speed else print(
            f'Автомобиль {self.name} движется слишком медленно, необходимо увеличить скорость на {self.min_speed - self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорось автомобиля {self.speed} км/ч') if self.speed <= 40 else print(
            f'Автомобиль {self.name} превысил скорость на {self.speed - 40} км/ч')


class PoliceCar(SportCar, Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


polo = TownCar(70, 'grey', 'Polo')
print(f'Полицейский автомобиль? - {polo.is_police}')
polo.go()
polo.turn('налево')
polo.show_speed()
polo.stop()

priora = PoliceCar(180, 'white', 'Priora')
print(f'Полицейский автомобиль? - {priora.is_police}')
priora.go()
priora.turn('налево')
priora.show_speed()
priora.stop()
