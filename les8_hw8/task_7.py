""" 7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных
чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата. """


class ComplexNumber(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumber(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return ComplexNumber(new_a, new_b)


z1 = ComplexNumber(2, 6)
z2 = ComplexNumber(5, 1)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)

# проверка корректнеости::
print(f'Проверка сложения: {complex(2, 6) + complex(5, 1)}')
print(f'Проверка умножения: {complex(2, 6) * complex(5, 1)}')

