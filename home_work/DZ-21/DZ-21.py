from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def show(self):
        print('Вывод на экран информации о фигуре')

    @staticmethod
    def save(file,  lst) -> None:
        with open(file=file, mode='w', encoding='utf-8') as f:
            for i in lst:
                f.writelines(str(i) + '\n')

    @staticmethod
    def load(file) -> list:
        lst_shapes = []
        try:
            with open(file=file, mode='r', encoding='utf-8') as f:
                text = f.readlines()
        except FileNotFoundError:
            print(f'Файл {file} не найден')
        else:
            for i in text:
                if not i.isspace():
                    line = i.split()
                    if line[0] == 'Square' and len(line) == 4:
                        lst_shapes.append(Square(int(line[1]),
                                                 int(line[2]),
                                                 int(line[3])))
                    elif line[0] == 'Rectangle' and len(line) == 5:
                        lst_shapes.append(Rectangle(int(line[1]),
                                                    int(line[2]),
                                                    int(line[3]),
                                                    int(line[4])))
                    elif line[0] == 'Circle' and len(line) == 4:
                        lst_shapes.append(Circle(int(line[1]),
                                                 int(line[2]),
                                                 int(line[3])))
                    elif line[0] == 'Ellipse' and len(line) == 5:
                        lst_shapes.append(Ellipse(int(line[1]),
                                                  int(line[2]),
                                                  int(line[3]),
                                                  int(line[4])))
        return lst_shapes


class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f'{self.__class__.__name__} {self.x} {self.y} {self.side}'

    def show(self):
        print(f'Квадрат, с координатами левого верхнего угла {self.x, self.y}, '
              f'длинной стороны - {self.side}')


class Rectangle(Shape):
    def __init__(self, x, y, side_a, side_b):
        self.x = x
        self.y = y
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f'{self.__class__.__name__} {self.x} {self.y} {self.side_a} {self.side_b}'

    def show(self):
        print(f'Прямоугольник, с координатами левого верхнего угла {self.x, self.y}, '
              f'сторонами {self.side_a} и {self.side_b}')


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f'{self.__class__.__name__} {self.x} {self.y} {self.radius}'

    def show(self):
        print(f'Окружность, с координатами центра {self.x, self.y}, '
              f'радиусом - {self.radius}')


class Ellipse(Shape):
    def __init__(self, x, y, side_a, side_b):
        self.x = x
        self.y = y
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f'{self.__class__.__name__} {self.x} {self.y} {self.side_a} {self.side_b}'

    def show(self):
        print(f'Эллипс, с координатами {self.x, self.y} левого верхнего угла '
              f'описанного вокруг него прямоугольника со сторонами - {self.side_a} и  {self.side_b}')


lst = [Square(25, 40, 30), Square(40, 40, 70),
       Rectangle(20, 20, 15, 35), Rectangle(40, 45, 50, 35),
       Circle(23, 26, 40), Circle(50, 50, 20),
       Ellipse(0, 10, 30, 30), Ellipse(5, 5, 45, 45)]
Shape.save('file.txt', lst)

print('--- Сохранили, теперь считываем в новый список ---')

new_lst = Shape.load('file.txt')
for i in new_lst:
    i.show()
