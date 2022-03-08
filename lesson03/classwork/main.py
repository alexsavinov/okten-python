# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
#

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return self.x * 2 + self.y * 2


r1 = Rectangle(20, 20)
r2 = Rectangle(10, 10)

print('-' * 40)
print('+ сума площадей двух экземпляров класса:', r1 + r2)
print('- разница площадей:', r1 - r2)
print('== или площади равны:', r1 == r2)
print('!= не равны:', r1 != r2)
print('< меньше:', r1 < r2)
print('> больше:', r1 > r2)
print('при вызове метода len() подсчитывать сумму сторон:', len(r1), len(r2))


# создать класс Human (name, age)
#
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} - {self.age}'

    def __repr__(self) -> str:
        return self.__str__()


# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки,
# так же должен быть метод который принимает лист золушек и ищет ту самую
#
# у класса золушки должна быть переменная
# count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество
#

class Cinderella(Human):
    count = 0

    @classmethod
    def inc_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size
        Cinderella.inc_count()

    def __str__(self) -> str:
        return f'Cinderella: {super().__str__()} ({self.size})'


class Prince(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self) -> str:
        return f'Prince: {super().__str__()} ({self.size})'

    def find(self, find_list: list[Cinderella]):
        for cinderella in find_list:
            if cinderella.size == self.size:
                return cinderella
        return None


prince1 = Prince('Arthur', 25, 35)
cinderellas_list = [Cinderella('Anna', 17, 34), Cinderella('Belle', 18, 35), Cinderella('Cindy', 19, 36)]
cinderella_find = prince1.find(cinderellas_list)

print('-' * 40)
print(prince1)
print(cinderellas_list)
print('сколько экземпляров класса золушка было создано:', Cinderella.get_count())
print('так же должен быть метод который принимает лист золушек и ищет ту самую:', cinderella_find)
