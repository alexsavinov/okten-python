# створити пустый список users_list = []
#
# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}

users_list = []
last_id = 0


def add_user():
    global last_id
    name = input('Введіть name (string): ')
    age = int(input('Введіть age: '))
    status = bool(input('Введіть status (1/0): '))
    last_id += 1
    user = {'id': last_id, 'name': name, 'age': age, 'status': status}
    users_list.append(user)


def show_users():
    if not len(users_list):
        print('Не додано жодного юзера!')
    for user in users_list:
        print(user)


def show_users_by_age():
    age = int(input('Введіть age для відбору: '))
    for user in users_list:
        if user['age'] == age:
            print(user)


def delete_user_by_id():
    id = int(input('Введіть id для відбору: '))
    for user in users_list:
        if user['id'] == id:
            users_list.remove(user)
            print(f'Видалено юзера з id={id}!')
            break


def change_user_status():
    id = int(input('Введіть id для відбору: '))
    for user in users_list:
        if user['id'] == id:
            user['status'] = not user['status']
            print(f'Змінено статус на {user["status"]} для юзера з id={id}!')
            break

while True:
    message = """
1) додававання нового юзера
2) вивід всіх юзерів
3) вивід всіх юзерів за віком
4) видалення юзера по id
5) заміна статуса юзера на протилежний
6) вихід з меню
Оберіть дію: """
    choice = int(input(message));
    print()

    if choice == 1:
        add_user()
    elif choice == 2:
        show_users()
    elif choice == 3:
        show_users_by_age()
    elif choice == 4:
        delete_user_by_id()
    elif choice == 5:
        change_user_status()
    elif choice == 6:
        print('', 'Вихід!', sep='\n')
        break
    else:
        print('', 'Введіть коректне число!', sep='\n')
