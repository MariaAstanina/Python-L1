# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class CountLim(Exception):
    def __init__(self, count, max_count):
        self.count = count
        self.max_count = max_count


class VolumeLim(Exception):
    def __init__(self, volume, max_volume):
        self.volume = volume
        self.max_volume = max_volume


class NotInStorage(Exception):
    def __init__(self, number, name):
        self.name = name
        self.number = number


class Storage:
    current_count = 0
    current_volume = 0
    equipment_book = {}

    def __init__(self, max_count, max_volume):
        self.max_count = max_count
        self.max_volume = max_volume

    def add_equipment(self, object, number):
        if self.current_count + number < self.max_count:
            self.current_count += number
        else:
            raise CountLim(number, self.max_count)

        if self.current_volume + object.volume * number > self.max_volume:
            raise VolumeLim(object.volume, self.max_volume)
        else:
            self.current_volume += object.volume * number
        self.equipment_book[object.model] = number
        print(f'Оборудование {object.model} в количестве {number}шт. принято на склад')

    def del_equipment(self, object, number):
        # print(self.equipment_book.get(object.model) - number)
        tmp = self.equipment_book.get(object.model) - number
        if tmp > 0:
            self.equipment_book[object.model] = self.equipment_book.get(object.model) - number
            print(
                f'Оборудование {object.model} в количестве {number}шт. выдано со склада, остаток: {self.equipment_book.get(object.model)} шт.')
        elif tmp == 0:
            self.equipment_book.pop(object.model)
            print(
                f'Оборудование {object.model} в количестве {number}шт. выдано со склада, остаток: 0 шт.')

        else:
            raise NotInStorage(number, object.model)

    def show_content(self):
        print(self.equipment_book)


class OfficeEquipment:
    equipment_counter = 0

    def __init__(self, model, volume, producer, price):
        self.model = model
        self.producer = producer
        self.price = price
        self.volume = volume
        OfficeEquipment.equipment_counter += 1

    def __str__(self):
        return f'Устройство {self.__name__}:/nМодель: {self.model}/nПроизводитель:{self.producer}/nСтоимость:{self.price}'


class Printer(OfficeEquipment):
    printer_counter = 0

    def __init__(self, model, volume, producer, price, print_speed, paper_size, isbluetooth=True):
        super().__init__(model, volume, producer, price)
        self.printer_speed = print_speed
        self.paper_size = paper_size
        self.isbluetooth = isbluetooth
        Printer.printer_counter += 1


class Scanner(OfficeEquipment):
    scanner_counter = 0

    def __init__(self, model, volume, producer, price, scanning_speed, paper_size, duplex_scanning=False):
        super().__init__(model, volume, producer, price)
        self.scanning_speed = scanning_speed
        self.paper_size = paper_size
        self.duplex_scanning = duplex_scanning
        Scanner.scanner_counter += 1


class Copier(OfficeEquipment):
    copier_counter = 0

    def __init__(self, model, volume, producer, price, copy_speed):
        super().__init__(model, volume, producer, price)
        self.copy_speed = copy_speed
        Copier.copier_counter += 1


def logger_del():
    def wrapper(*args, **kwargs):
        print(f'-- Запрос на выдачу оборудования {args[0].model} в количестве {args[1]} шт.')
        try:
            my_storage.del_equipment(*args, **kwargs)
        except NotInStorage:
            print(f'Ошибка: оборудование {args[0].model} отсутствует на складе в необходимом количестве')

    return wrapper


def logger_add():
    def wrapper(*args, **kwargs):
        print(f'-- Запрос на добавление оборудования {args[0].model} в количестве {args[1]} шт. на склад')
        try:
            my_storage.add_equipment(*args, **kwargs)
        except {VolumeLim, CountLim}:
            print(f'Ошибка: оборудование {args[0].model} отсутствует на складе в необходимом количестве')

    return wrapper


my_storage = Storage(30, 25)

scaner_1 = Scanner('model1', 1, 'brother', 10_000, 60, 'A4')
scaner_2 = Scanner('model2', 2, 'brother', 10_000, 60, 'A4')

log_add = logger_add()
log_add(scaner_1, 10)
log_add(scaner_2, 6)
my_storage.show_content()
log_del = logger_del()
for _ in range(0, 7):
    log_del(scaner_1, 3)
    log_del(scaner_2, 2)
    my_storage.show_content()
