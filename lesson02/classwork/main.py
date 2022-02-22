# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции
#

def decor(func):
    counter = 0

    def wrapper():
        nonlocal counter
        counter += 1
        print('count:', counter)
        func()
        print(20 * '-')

    return wrapper


print(50 * '*', 'сколько раз была запущена функция (calls):', 50 * '*', sep='\n')


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
func2()


# кому это очень легко то сделайте функцию на замыкания которая будет возвращать декоратор
# который будет считать общее количество запущенных  функций декорированных этим декоратором
#

def decor2(func, func_calls={}):
    func_calls[func] = 0

    def wrapper():
        func_calls[func] += 1
        print('decor calls:', sum(func_calls.values()))
        func()
        print(20 * '-')

    return wrapper


print(50 * '*',
      'общее количество запущенных функций декорированных этим декоратором (decor calls):',
      50 * '*',
      sep='\n')


@decor2
def func3():
    print('func3')


@decor2
def func4():
    print('func4')


func3()
func3()
func4()
func3()
func4()
