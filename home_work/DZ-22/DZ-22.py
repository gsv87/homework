from math import pi


# Задание 1


class Circle:
    def __init__(self, radius):
        if radius >= 0:
            self.radius = radius
            self.perimetr = self.__get_perimetr()
        else:
            raise Exception('Ошибка. Радиус отрицательный')

    def __get_perimetr(self):
        return round(2 * pi * self.radius, 2)

    def __str__(self):
        return f'Окружность с радиусом {self.radius} и длиной окружности {self.perimetr}'

    def __eq__(self, other: 'Circle'):
        return self.radius == other.radius

    def __lt__(self, other: 'Circle'):
        return self.perimetr < other.perimetr

    def __le__(self, other: 'Circle'):
        return self.perimetr <= other.perimetr

    def __gt__(self, other: 'Circle'):
        return self.perimetr > other.perimetr

    def __ge__(self, other: 'Circle'):
        return self.perimetr >= other.perimetr

    def __add__(self, other: int | float):
        self.radius += other
        self.perimetr = self.__get_perimetr()
        return Circle(self.radius)

    def __sub__(self, other: int | float):
        if self.radius >= other:
            self.radius -= other
            self.perimetr = self.__get_perimetr()
            return Circle(self.radius)
        else:
            raise Exception('Вычитаемый радиус больше текущего')


# Задание 2


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        znak = '+'
        if self.re == 0 and self.im == 0:
            result = '0'
        elif self.re == 0:
            result = f'{self.im}i'
        elif self.im == 0:
            result = f'{self.re}'
        else:
            if self.im < 0:
                znak = '-'
            result = f'{self.re}{znak}{abs(self.im) if self.im not in (1, -1) else ""}i'
        return result

    def __add__(self, other: 'Complex'):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: 'Complex'):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other: 'Complex'):
        return Complex(self.re * other.re - self.im * other.im,
                       self.im * other.re + self.re * other.im)

    def __truediv__(self, other: 'Complex'):
        if other.re == 0 and other.im == 0:
            raise ZeroDivisionError('Ошибка. Деление на ноль')
        znamenatel = other.re ** 2 + other.im ** 2
        new_re = (self.re * other.re + self.im * other.im) / znamenatel
        new_im = (self.im * other.re - self.re * other.im) / znamenatel
        return Complex(round(new_re, 2), round(new_im, 2))


# Задание 3


class Airplane:
    def __init__(self, type: str, max_passengers: int, passengers: int = 0):
        self.type = type
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __str__(self):
        return f'Самолет "{self.type}" ' \
               f'макс количество пассажиров {self.max_passengers} ' \
               f'пассажиров в салоне {self.passengers}'

    def __eq__(self, other: 'Airplane'):
        return self.type == other.type

    def __add__(self, other: int):
        if (self.passengers + other) <= self.max_passengers:
            self.passengers += other
            return Airplane(self.type, self.max_passengers, self.passengers)
        else:
            raise Exception('Превышено макс количество пассажиров')

    def __sub__(self, other: int):
        if (self.passengers - other) >= 0:
            self.passengers -= other
            return Airplane(self.type, self.max_passengers, self.passengers)
        else:
            raise Exception('Количество пассажиров отрицательно')

    def __lt__(self, other: 'Airplane'):
        return self.max_passengers < other.max_passengers

    def __le__(self, other: 'Airplane'):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other: 'Airplane'):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other: 'Airplane'):
        return self.max_passengers >= other.max_passengers


# Задание 4


class Flat:

    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __str__(self):
        return f'Квартира площадью {self.area} и ценой {self.price}'

    def __eq__(self, other: 'Flat'):
        return self.area == other.area

    def __ne__(self, other: 'Flat'):
        return self.area != other.area

    def __lt__(self, other: 'Flat'):
        return self.price < other.price

    def __le__(self, other: 'Flat'):
        return self.price <= other.price

    def __gt__(self, other: 'Flat'):
        return self.price > other.price

    def __ge__(self, other: 'Flat'):
        return self.price >= other.price
