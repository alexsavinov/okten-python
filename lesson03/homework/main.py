# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
#
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
#

class Book(Printable):
    def print(self):
        print("!!")


class Magazine(Printable):
    def print(self):
        print("!!!!")

# 3) Створити свій кастомний Exception
#


# 4) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#


# 4)всі методи класу Main запускати в try except, приклад:
# try:
#     Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazineі()
#     print('-' * 40)
#
