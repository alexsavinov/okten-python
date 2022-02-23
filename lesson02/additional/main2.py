# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
#
def fib(num: int) -> str:
    fib1 = fib2 = 1
    list_fib = [str(fib1), str(fib2)]
    for i in range(2, num):
        fib1, fib2 = fib2, fib1 + fib2
        list_fib.append(str(fib2))
    return ' '.join(list_fib)


print(50 * '*', 'вивести послідовність Фібоначі, кількість вказана в знінній:', sep='\n')
print(fib(10))


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
#
def pnp(num: int) -> str:
    n = p = 0
    for i in str(num):
        if int(i) % 2:
            n += 1
        else:
            p += 1

    return f'п = {p}, н = {n}'


print(50 * '*', 'порахувати кількість парних і непарних цифр числа:', sep='\n')
print(pnp(112198))


# прога, що виводить кількість кожного символа з введеної строки, наприклад:
# st = 'as 23 fdfdg544'  # введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
#
def symbols_count(string: str) -> None:
    total = {}
    for i in range(len(string)):
        counter = total.get(string[i], 0) + 1
        total.update({string[i]: counter})
    for key, item in total.items():
        print(f'\'{key}\' -> {item}')


print(50 * '*', 'прога, що виводить кількість кожного символа з введеної строки:', sep='\n')
symbols_count('as 23 fdfdg544')


# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
#
def list_odd(size: int = 0) -> list:
    return [i for i in range(size * 2) if i % 2]


def list_of_lists(arg_list: list) -> list[list]:
    res_list = []
    i = 0
    size = 0
    while i < len(arg_list):
        size += 1
        n = 0
        inner_list = []
        while n < size and i != len(arg_list):
            inner_list.append(arg_list[i])
            i += 1
            n += 1
        res_list.append(inner_list)
    return res_list


print(50 * '*', 'лист листов:', sep='\n')

print(list_odd(14))
print(list_of_lists(list_odd(14)))

print(list_of_lists([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
print(list_of_lists([1, 3, 5, 7, 9, 11]))
print(list_of_lists([1, 3, 5, 7, 9]))
print(list_of_lists([1, 3, 5, 7, 9, 11, 13]))
