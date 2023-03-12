from re import fullmatch


def check_type(type_data=int):
    def decorator(func):
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, type_data):
                    raise TypeError(f'Тип данных должен быть {type_data}, а не {type(arg)}')
            return func(*args)
        return wrapper
    return decorator


class Date:

    @check_type()
    def __init__(self, day, month, year):
        self.__year = year
        if month <= 0 or month > 12:
            raise ValueError(f'Введите месяц от 1 до 12')
        self.__month = month
        days = self.days_in_month()
        if day <= 0 or day > days:
            raise ValueError(f'Введите день от 1 до {days}')
        self.__day = day

    def __str__(self):
        if self.__year < 0:
            return f'{str(self.__day).rjust(2, "0")}.{str(self.__month).rjust(2, "0")}.{abs(self.__year)} до н.э.'
        return f'{str(self.__day).rjust(2, "0")}.{str(self.__month).rjust(2, "0")}.{self.__year}'

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @year.setter
    @check_type()
    def year(self, year: int):
        self.__year = year

    @month.setter
    @check_type()
    def month(self, month: int):
        if month <= 0 or month > 12:
            raise ValueError(f'Введите месяц от 1 до 12')
        self.__month = month

    @day.setter
    @check_type()
    def day(self, day: int):
        days = self.days_in_month()
        if day <= 0 or day > days:
            raise ValueError(f'Введите день от 1 до {days}')
        self.__day = day

    def is_leap_year(self):
        return self.__year % 400 == 0 or (self.__year % 4 == 0 and self.__year % 100 != 0)

    def days_in_month(self):
        if self.__month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif self.__month in (4, 6, 9, 11):
            return 30
        elif self.__month == 2 and self.is_leap_year():
            return 29
        else:
            return 28

    def next_day(self):
        if self.__day < self.days_in_month():
            self.__day += 1
        elif self.__month < 12:
            self.__day = 1
            self.__month += 1
        else:
            self.__day = 1
            self.__month = 1
            self.__year += 1
    # Доп условие для года до нашей эры по моему не требуется, т.к.
    # в атрибуте класса год до нашей эры хранится со знаком минус.
    # Например дата 31.12.100 до нашей эры (day=31, month=12, year=-100),
    # при вызове метода next_day(), day будет = 1, month тоже 1,
    # а year -100 + 1 = -99. В методе __str__ значение года вывожу по модулю.
    # Результат выввода будет 01.01.99 до н.э

    def set_date(self, line='01-01-1234'):
        # Сначала пришла идея написать регулярное выражение с название
        # групп (?P<name>....) чтобы уместить оба варианта "гггг-мм-дд" и
        # "дд-мм-гггг" в одном выражении, но код очень длинный получился.
        # Оставил вариант без названий просто с группировкой. Не знаю как
        # принято писать, по этому оставил оба варианта))
        # date = fullmatch(r'((?P<d>\d\d)\W(?P<m>\d\d)\W(?P<y>\d{4}))|((?P<y1>\d{4})\W(?P<m1>\d\d)\W(?P<d1>\d\d))', line)
        # if date:
        #     day = date['d'] if date['d'] else date['d1']
        #     month = date['m'] if date['m'] else date['m1']
        #     year = date['y'] if date['y'] else date['y1']
        date = fullmatch(r'((\d\d)\W(\d\d)\W(\d{4}))|((\d{4})\W(\d\d)\W(\d\d))', line)
        if date:
            day = date[2] if date[2] else date[8]
            month = date[3] if date[3] else date[7]
            year = date[4] if date[4] else date[6]
            if int(month) > 12:
                if int(day) <= 12:
                    month, day = day, month
                else:
                    raise ValueError('Некоректная дата')
            # Проверки перед установкой даты не делал, т.к. они есть в сеттерах,
            # главное первым установить год, потом месяц и последним день, чтобы
            # проверки в сеттерах отработали корректно
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
