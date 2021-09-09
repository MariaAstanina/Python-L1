class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'{self.a} + {self.b}i'


cn_1 = ComplexNum(1, -2)
cn_2 = ComplexNum(3, 4)
print(cn_1)
print(cn_1 + cn_2)
print(cn_1 * cn_2)
