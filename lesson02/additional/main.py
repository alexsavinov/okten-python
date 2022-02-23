import functools


# Cоздать функцию которая принимает число и возвращает  текст как в примере:
#     3275  —>  "3000 + 200 + 70 +5"
#
def expanded_form(num: int) -> str:
    str_num = str(num)
    list_digits: list = [f'{n}{("0" * (len(str_num) - i - 1))}' for i, n in enumerate(str_num) if n != '0']
    return ' + '.join(list_digits)


print(50 * '*', 'Cоздать функцию которая принимает число и возвращает текст как в примере:', sep='\n')
print(expanded_form(70304))


# Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
# Всегда будет только одно целое число, которое встречается нечетное количество раз
#     [1,2,3,4,5,2,4,1,3] -> 5
#
def even_number(arg_list: list) -> list:
    return [i for i in set(arg_list) if arg_list.count(i) % 2 != 0][0]


test_list: list = [1, 2, 3, 4, 5, 2, 4, 1, 3]

print(50 * '*', 'Дан массив целых чисел, найдите тот, который встречается нечетное количество раз:', sep='\n')
print(even_number(test_list))


# Знайти анаграму.
#     Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
#
#     ANAGRAM | MGANRAA -> true
# EXIT | AXET -> false
# GOOD | DOGO -> true
#
def anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


print(50 * '*', 'Знайти анаграму. Перевірити чи слово має в собі такі самі літери як і поеперднє слово:', sep='\n')
print(anagram('ANAGRAM', 'MGANRAA'))
print(anagram('EXIT', 'AXET'))
print(anagram('GOOD', 'GOOD'))


# Точная степень двойки
# Дано натуральное число N.
#     Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#     Операцией возведения в степень пользоваться нельзя!
#
def is_pow_of_two(num: int) -> str:
    if num % 2 != 0:
        return 'NO'

    while num % 2 == 0 or num == 2:
        num = num / 2

    if int(num) == 1:
        return 'YES'

    return 'NO'


print(50 * '*', 'Точная степень двойки. Выведите слово YES, если число N является точной степенью двойки:', sep='\n')
print(is_pow_of_two(96))
print(is_pow_of_two(32))


#  Сумма цифр числа
# Дано натуральное число N. Вычислите сумму его цифр.
#     При решении этой задачи нельзя использовать строки,
#     списки, массивы ну и циклы, разумеется.
#     Рекурсія)
#
def recur_sum_of_digits(number: int) -> float | int:
    if number:
        return (number % 10) + recur_sum_of_digits(number // 10)
    else:
        return 0


print(50 * '*', 'Сумма цифр числа. Дано натуральное число N. Вычислите сумму его цифр:', sep='\n')
print(recur_sum_of_digits(81))
print(recur_sum_of_digits(9000000000000))


# Палиндром
# Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово палиндромом. Выведите YES или NO.
#     При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя использовать срезы с шагом, отличным от 1.
#
def is_palindrome(string: str) -> str:
    reversed_string = ''.join(reversed(string))
    if reversed_string == string:
        print('YES')
    else:
        print('NO')


print(50 * '*', 'Палиндром. Проверьте, является ли это слово палиндромом:', sep='\n')
print(is_palindrome('topot'))


# Количество единиц
# Дана последовательность натуральных чисел  в строке, завершающаяся двумя числами 0 подряд.
# Определите, сколько раз в этой последовательности встречается число 1. Числа, идущие после двух нулей, необходимо игнорировать.
#
# 2176491947586100 -> 3
#
def number_of_one(num: int) -> int:
    return str(num).count('1');


print(50 * '*', 'Количество единиц. сколько раз в этой последовательности встречается число 1:', sep='\n')
print(number_of_one(2176491947586100))


# Вирівняти багаторівневий масив в однорівневий
#     [1,3, ['Hello, 'Wordd', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'Wordd', 9, 6, 1, 'oops', 9]
# flat використовувати заборонено.
#
def recur_flat(arg_list: list = [], arr: list = []) -> list:
    for i in arg_list:
        if isinstance(i, list):
            recur_flat(i, arr)
        else:
            arr.append(i)

    return arr


test_list2 = [1, 3, ['Hello', 'World', [9, 6, 1]], ['oops'], 9]

print(50 * '*', 'Вирівняти багаторівневий масив в однорівневий:', sep='\n')
print(recur_flat(test_list2))


# Знайти набільший елемент в масиві за допомогою reduce
#     [1,6,9,0,17,88,4,7] -> 88
#
def max_val(arg_list: list = []) -> int:
    return functools.reduce(lambda a, b: b if a < b else a, arg_list)


test_list3 = [1, 6, 9, 0, 17, 88, 4, 7]

print(50 * '*', 'Знайти набільший елемент в масиві за допомогою reduce:', sep='\n')
print(max_val(test_list3))
