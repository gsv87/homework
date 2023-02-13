from random import randint

# 6.
# Дан массив целых чисел,
# отсортируйте массив в порядке
# возрастания в зависимости от
# частоты значений.
# Вернуть отсортированный массив.
# lst = [2, 1, 2, 2, 1, 3] => [3, 1, 1, 2, 2, 2]


def sorted_list(spis):
    dict_quantity = {i: spis.count(i) for i in spis}
    return sorted(sorted(spis), key=lambda elem: dict_quantity[elem])


lst_1 = [2, 1, 2, 2, 1, 3]
print(lst_1, '=>', sorted_list(lst_1))
lst_2 = [2, 3, 3, 4, 1, 2, 4, 3, 6, 7, 4, 6, 6, 3]
print(lst_2, '=>', sorted_list(lst_2))


# 7.
# Вам дан массив nums, состоящий
# из целых положительных чисел.
# Вы должны взять каждое целое число
# в массиве, поменять местами его цифры
# и добавить новое число в конец массива.
# По итогу надо вернуть количество уникальных
# целых чисел в конечном массиве.


def reverse_number(number):
    return int(''.join([i for i in str(number)][::-1]))


# nums = [randint(1000, 9999) for i in range(10)]
nums = [2587, 4467, 9633, 7510, 2587, 4567, 2587, 6376, 6128, 1828]
a = len(nums)
for i in range(a):
    nums.append(reverse_number(nums[i]))
print(len(set(nums)))


# 8.
# Дан массив целых чисел nums.
# Верните максимальное значение такое, что:
# (nums[i]-1)*(nums[j]-1).

#  Можно было отсортировать список по убыванию и первые два элемента перемножить,
#  но это сработает только с положительными числами. Может получится так что при
#  умножении двух отрицательных чисел как раз и будет максимальное значение,
#  по этому пришлось через перебор всех возможных пар умножений


def find_max_multiplication(spis):
    max_multiplication = min(spis)
    for i in range(len(spis)):
        for j in range(i + 1, len(spis)):
            if (spis[i] - 1) * (spis[j] - 1) > max_multiplication:
                max_multiplication = (spis[i] - 1) * (spis[j] - 1)
    return max_multiplication


nums_1 = [-63, -43, 9, 55, 42, -83, 46, -9, 61, -33]
nums_2 = [randint(1, 100) for i in range(10)]
print(nums_1)
print(find_max_multiplication(nums_1))
print(nums_2)
print(find_max_multiplication(nums_2))
