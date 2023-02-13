class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.denominator == 1:
            return f'{self.numerator}'
        return f'{self.numerator}/{self.denominator}'

    @staticmethod
    def find_nod(a, b):
        if a == 0 or b == 0:
            return 1
        if a % b == 0:
            return b
        return Fraction.find_nod(b, a % b)

    def get_data(self):
        return self.numerator, self.denominator

    def print_fraction(self):
        print(f'{self.numerator}/{self.denominator}')

    def reset(self):
        self.numerator = int(input('Введите новый числитель: '))
        self.denominator = int(input('Введите новый знаменатель: '))

    def sum(self, another: 'Fraction'):
        denom = self.denominator * another.denominator
        num = self.numerator * another.denominator + \
            another.numerator * self.denominator
        nod = Fraction.find_nod(num, denom)
        return Fraction(num // nod, denom // nod)

    def subtraction(self, another: 'Fraction'):
        denom = self.denominator * another.denominator
        num = self.numerator * another.denominator - \
            another.numerator * self.denominator
        nod = Fraction.find_nod(num, denom)
        return Fraction(num // nod, denom // nod)

    def multiplication(self, another: 'Fraction'):
        denom = self.denominator * another.denominator
        num = self.numerator * another.numerator
        nod = Fraction.find_nod(num, denom)
        return Fraction(num // nod, denom // nod)

    def division(self, another: 'Fraction'):
        denom = self.denominator * another.numerator
        num = self.numerator * another.denominator
        nod = Fraction.find_nod(num, denom)
        return Fraction(num // nod, denom // nod)


a = Fraction(3, 4)
b = Fraction(7, 8)
a.print_fraction()
b.print_fraction()
print(a.sum(b))
print(a.subtraction(b))
print(a.multiplication(b))
print(a.division(b))


# Задание 2
# Реализовать иерархию классов:

class GroundTransport:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show_info(self):
        print(f'Модель: {self.model}\n'
              f'Цвет: {self.color}')

    def reset_info(self, model, color):
        self.model = model
        self.color = color


class WheeledTransport(GroundTransport):
    def __init__(self, model, color, max_speed=0):
        super().__init__(model, color)
        self.max_speed = max_speed

    def show_info(self):
        print(f'Модель: {self.model}\n'
              f'Цвет: {self.color}\n'
              f'Максимальная скорость: {self.max_speed}')


class TrackedVehicles(GroundTransport):
    def __init__(self, model, color, load_capacity=0):
        super().__init__(model, color)
        self.load_capacity = load_capacity

    def get_attr(self):
        return self.model, self.color, self.load_capacity

    def set_attr(self, model, color, load_capacity):
        self.model = model
        self.color = color
        self.load_capacity = load_capacity

    def show_info(self):
        super().show_info()
        print(f'Грузоподъемность: {self.load_capacity}')


class AirCushionTransport(GroundTransport):
    def __init__(self, model, color):
        GroundTransport.__init__(self, model, color)


obj_1 = GroundTransport('Vaz', 'red')
obj_2 = WheeledTransport('mazda cx-5', 'orange', 220)
obj_3 = TrackedVehicles('Нептун 23GR', 'black', 1450)
print(obj_1.show_info())
print(obj_2.show_info())
print(obj_3.show_info())
