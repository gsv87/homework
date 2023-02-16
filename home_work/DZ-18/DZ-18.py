# Задание 1
# К уже реализованному классу «Дробь» добавьте ста-
# тический метод, который при вызове возвращает коли-
# чество созданных объектов класса «Дробь».

class Fraction:
    __counter = 0

    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.__counter += 1

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

    @staticmethod
    def get_counter():
        return Fraction.__counter

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
c = Fraction(3, 3)
print(Fraction.get_counter())


# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фа-
# ренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.

class ConversionTemp:
    __counter = 0

    def __init__(self, temp):
        self.temp = temp

    @staticmethod
    def get_counter():
        return ConversionTemp.__counter

    @staticmethod
    def c_to_f(temp):
        ConversionTemp.__counter += 1
        return temp * 1.8 + 32

    @staticmethod
    def f_to_c(temp):
        ConversionTemp.__counter += 1
        return (temp - 32) / 1.8


print(ConversionTemp.c_to_f(10))
print(ConversionTemp.f_to_c(50))
print(ConversionTemp.c_to_f(10))
print(ConversionTemp.get_counter())


# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class Length:
    # Словарь содержит два ключа 'a' - английская система мер длины, 'm' - метрическая.
    # Значения это еще один словарь содержащий в ключах меры длинны, а в значениях записано
    # число для перевода в минимальную меру длинны (mm или inch), то есть 1 yard это 36 inch,
    # 1 foot - 12 inch, 1 m - 1000 mm, 1 sm - 10mm и тд.
    slovar = {'a': {'inch': 1, 'foot': 12, 'yard': 36, 'mile': 63360},
              'm': {'mm': 1, 'sm': 10, 'm': 1000, 'km': 1000000}}

    @staticmethod
    def convert(system, measure, value, output_measure):
        # system - система мер длинны, measure - мера длинны из котрой переводим,
        # value - переводимое значение, output_measure - мера длинны в которую переводим.
        # Метод сделал так что введенное значение value перевожу в минимальную меру длинны
        # (mm или inch), потом перевожу в противоположную систему мер длинны, путем умножения
        # на коэффициент 'к' ('к' это отношение mm к inch или inch к mm). Полученное значение
        # перевожу в необходимую меру длинны. Напрмер: 10 foot перевести в sm, перевожу foot
        # в inch  10 * 12 = 120 inch, далее inch в mm  120 * 25.4 = 3048 mm и делим на 10
        # чтобы получить sm 3048 / 10 = 304.8 sm
        reverse_system = 'a' if system == 'm' else 'm'
        k = 1/25.4 if system == 'm' else 25.4
        return value * Length.slovar[system][measure] * k / Length.slovar[reverse_system][output_measure]


def length_converter():
    while True:
        otvet = input('Хотите перевести еще раз? (yes/no): ')
        if otvet == 'yes':
            while True:
                system_of_measures = input('Из какой системы мер хотите перевести? a - английская, m - метрическая: ')
                if system_of_measures in Length.slovar.keys():
                    spis = '/'.join(Length.slovar[system_of_measures].keys())
                    break

            while True:
                measure = input(f'Введите меру длины ({spis}): ')
                if measure in Length.slovar[system_of_measures].keys():
                    reverse_system = 'a' if system_of_measures == 'm' else 'm'
                    reverse_spis = '/'.join(Length.slovar[reverse_system].keys())
                    break

            while True:
                output_measure = input(f'В какую меру длинны перевести ({reverse_spis}): ')
                if output_measure in Length.slovar[reverse_system].keys():
                    break

            while True:
                value = input('Введите значение: ')
                if value.isdigit():
                    result = Length.convert(system_of_measures, measure, int(value), output_measure)
                    print(f'{value} {measure} = {result} {output_measure}')
                    break
        elif otvet == 'no':
            print('Пока')
            break


print(Length.convert('a', 'foot', 10, 'sm'))
print(Length.convert('m', 'm', 12, 'inch'))

if __name__ == '__main__':
    length_converter()
