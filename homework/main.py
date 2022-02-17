# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
#
string1 = 'as 23 fdfdg544'
# string1 = input()
res = ([i for i in string1 if i.isdigit()])
print(50 * '*', 'вибирає зі введеної строки цифри і виводить їх через кому', sep='\n')
print(','.join(res))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
#
string2 = 'as 23 fdfdg544 34'
# string2 = input()
prev, res = '', ''
for i in range(len(string2)):
    val = string2[i]
    if string2[i].isdigit():
        res += val
    elif i == len(string2) - 1 or not prev.isdigit():
        res += ''
    else:
        res += ', '
    prev = val
print(50 * '*', 'вибирає зі введеної строки числа і виводить їх так як вони написані', sep='\n')
print(res)

# #################################################################################
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
greeting = 'Hello, world'
res = [i.upper() for i in greeting]
print(50 * '*', 'записать каждый символ в лист поменяв его на верхний регистр', sep='\n')
print(res)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
res = [pow(i, 2) for i in range(50) if i % 2]
print(50 * '*', 'с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат', sep='\n')
print(res)


# function
#
# - створити функцію яка виводить ліст
#
def print_list(arg):
    print(arg)


print(50 * '*', 'створити функцію яка виводить ліст', sep='\n')
print_list([1, 22, 333])


# - створити функцію яка приймає три числа та виводить та повертає найменьше.
#
def print_min(d1, d2, d3):
    res = min(d1, d2, d3)
    print(res)
    return res


print(50 * '*', 'створити функцію яка приймає три числа та виводить та повертає найменьше', sep='\n')
print_min(111, 22, 333)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
#
def print_max(d1, d2, d3):
    res = max(d1, d2, d3)
    print(res)
    return res


print(50 * '*', 'створити функцію яка приймає три числа та виводить та повертає найбільше', sep='\n')
print_max(111, 22, 333)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
#
def print_max_return_min(*args):
    print(f'max: {max(args)}')
    return f'min: {min(args)}'


print(50 * '*', 'приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше', sep='\n')
print(print_max_return_min(111, 22, 333, 4444))


# - створити функцію яка повертає найбільше число з ліста
#
def max_list(arg_list):
    return max(arg_list)


print(50 * '*', 'створити функцію яка повертає найбільше число з ліста', sep='\n')
print(max_list([111, 22, 333, 4444]))


# - створити функцію яка повертає найменьше число з ліста
#
def min_list(arg_list):
    return min(arg_list)


print(50 * '*', 'створити функцію яка повертає найменьше число з ліста', sep='\n')
print(min_list([111, 22, 333, 4444]))


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
def sum_list(arg_list):
    return sum(arg_list)


print(50 * '*', 'приймає ліст чисел та складає значення елементів ліста та повертає його', sep='\n')
print(sum_list([111, 22, 333, 4444]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
def avg_list(arg_list):
    return sum(arg_list) / len(arg_list) if len(arg_list) else 0


print(50 * '*', 'приймає ліст чисел та повертає середнє арифметичне його значень', sep='\n')
print(avg_list([111, 22, 333, 4444]))

# #################################################################################################
# 1) Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
#
my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

print(50 * '*', '- найти min число в листе', sep='\n')
print(min(my_list))
print('- удалить все дубликаты в листе', sep='\n')
print(list(set(my_list)))
print('- заменить каждое четвертое значение на "Х"', sep='\n')
print([v if (i + 1) % 4 else 'X' for i, v in enumerate(my_list)])


# 2) вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
def square(a):
    for i in range(0, a):
        for j in range(0, a):
            print('*' if not i or not j or i == a - 1 or j == a - 1 else ' ', end='')
        print()


print(50 * '*', 'вывести на экран пустой квадрат из "*" сторона которого указана в переменой', sep='\n')
square(3)


# 3) вывести табличку умножения с помощью цикла while
#
def multiple_table(x=1, y=1):
    while x < 10:
        while y < 10:
            print(str(x * y).rjust(3), end=' ')
            y += 1
        print()
        y = 1
        x += 1


print(50 * '*', 'вывести табличку умножения с помощью цикла while', sep='\n')
multiple_table()

# 4) переделать первое задание под меню с помощью цикла
#
while True:
    message = """
1. найти min число в листе
2. удалить все дубликаты в листе
3. заменить каждое четвертое значение на "Х"
0. выход
Сделайте свой выбор: """
    choice = int(input(message));

    if choice == 1:
        print('', min(my_list), sep='\n')
    elif choice == 2:
        print('', list(set(my_list)), sep='\n')
    elif choice == 3:
        print('', [v if (i + 1) % 4 else 'X' for i, v in enumerate(my_list)], sep='\n')
    elif choice == 0:
        print('', 'Выход!', sep='\n')
        break
    else:
        print('', 'Введите корректное число!', sep='\n')


# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4l
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
#

my_list2 = [-1, -2, 3, 4, 555]


def closet_avg(arg_list):
    res = dict((abs((sum(arg_list) / len(arg_list) if len(arg_list) else i) - i), i) for i in arg_list)
    return res[min(res.keys())]


print(50 * '*',
      'вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа',
      sep='\n')
print(closet_avg(my_list2))