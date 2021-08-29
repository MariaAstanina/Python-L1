# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix_list=[]):
        self.matrix_list = matrix_list
        matrix_len = set(map(len, matrix_list))
        if len(matrix_len) > 1:
            print("\033[31m {}".format('Ошибка: введенные данные невозможно преобразовать в матрицу'))

    def __str__(self):
        return '\n'.join([' '.join(map(str, list)) for list in self.matrix_list])

    def __add__(self, other):
        return [[self.matrix_list[i][j] + other.matrix_list[i][j] for j in range
        (len(self.matrix_list[0]))] for i in range(len(self.matrix_list))]


m = Matrix([[1, 2, 5], [0, 2, 4]])
n = Matrix([[1, 2, 5], [0, 2, 4]])
new = Matrix(m + n)
print(new)
