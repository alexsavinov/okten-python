# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
#
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        print(f'Printable: {self.name}')


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та які наслідуються від класу Printable
#
class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        pass


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        pass


# 3) Створити свій кастомний Exception
#
class NonBookMagazineException(Exception):
    pass


# 4) Створити клас Main в якому буде:
# - змінна класу printable_list, яка буде зберігати книжки та журнали
# - метод add, за допомогою якого можна додавати екземпляри класів в список
#   і робити перевірку чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
# - метод show_all_magazines, який буде виводити всі журнали викликаючи метод print абстрактного класу
# - метод show_all_books, який буде виводити всі книги викликаючи метод print абстрактного класу
#
class Main:
    printable_list: list[Book | Magazine] = []

    @classmethod
    def add(cls, item):
        if not isinstance(item, Book | Magazine):
            raise NonBookMagazineException
        cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                super(Magazine, item).print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                super(Book, item).print()


# 5) всі методи класу Main запускати в try except, приклад:
# try:
#     Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
# except NonBookMagazineException:
#     print('Це не журнал або книжка')
# except Exception as err:
#     print(err)
#

try:
    Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
    print('-' * 40)

    Main.add('some test incorrect data')
except NonBookMagazineException:
    print('Це не журнал або книжка')
except Exception as err:
    print(err)
