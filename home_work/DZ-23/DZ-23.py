from functools import reduce

# Задание 1
# Напишите лямбда-функцию, которая принимает строку и
# возращает копию строки с удаленными гласными

line = 'Hello world. How beautiful you are'
new_stroka = lambda line: ''.join([x for x in line if x.lower() not in 'aeyuio'])
print(new_stroka(line))


# Задание 2
# Напишите лямбда-функцию, которая принимает строку и
# возращает True, если она содержит только буквы алфавита
# и False в противном случае

line = 'Hello world. How beautiful you are'
line_1 = 'HelloworldHowbeautifulyouare'
line_2 = 'Hello 6 world '
foo = lambda line: line.isalpha()
print(foo(line))
print(foo(line_1))
print(foo(line_2))


# Задание 3
# Напишите лямбда-функцию, которая принимает список целых
# чисел и возращает произведение всех чисел


numbers = [1, 2, 3, 4, 5]
multiplication_numbers = reduce(lambda a, b: a * b, numbers)
print(multiplication_numbers)


# Задание 4
# Напишите лямбда-функцию, которая принимает список строк и
# возращает новый список, содержащий только строки, являющиеся
# палиндромами

lst_line = ['qwerty', 'asddsa', 'privet', 'No lemon, no melon']
new_lst = lambda lst: [x for x in lst if x.lower().replace(' ', '') == x.lower().replace(' ', '')[::-1]]
new_lst1 = lambda lst: [x for x in lst if x.lower().replace(' ', '') == ''.join(reversed(x.lower().replace(' ', '')))]
print(new_lst(lst_line))
print(new_lst1(lst_line))


# Задание 5
# Напишите лямбда-функцию, которая принимает число и возращает True,
# если это простое число и False в противном случае

simple_num = lambda num: False if num in (0, 1) else not bool([x for x in range(2, num) if num % x == 0])
print(simple_num(0))
print(simple_num(1))
print(simple_num(2))
print(simple_num(3))
print(simple_num(4))


# Задание 6
# Напишите лямбда-функцию, которая принимает число и
# возращает его факториал

fact_num = lambda num: 1 if num == 1 else num * fact_num(num - 1)
print(fact_num(5))
num = 5
fact_num1 = reduce(lambda x, y:  x * y, [i for i in range(1, num + 1)])
print(fact_num1)
