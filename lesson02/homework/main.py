# 1) написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
# запишите 5 тудушек
# и выведете все
#
from typing import Callable


def notebook():
    todo_list = []

    def add_todo(todo):
        todo_list.append(todo)

    def get_all():
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()

add_todo(1)
add_todo(True)
add_todo('test todo item')
add_todo(None)
add_todo({'test todo item2': 1.0})

print(get_all())


# 2) протипизировать первое задание
#

def notebook_t() -> tuple[Callable]:
    todo_list = []

    def add_todo_t(todo: str) -> None:
        todo_list.append(todo)

    def get_all_t() -> list[str]:
        return todo_list

    return add_todo_t, get_all_t


add_todo_t, get_all_t = notebook_t()

add_todo_t('1')
add_todo_t('3')
add_todo_t('test todo')
add_todo_t('test todo2')
add_todo_t('test todo3')

print(get_all_t())


# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# Пример:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    str_num = str(num)
    list_digits = [f'{n}{("0" * (len(str_num) - i - 1))}' for i, n in enumerate(str_num) if n != '0']
    return ' + '.join(list_digits)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
