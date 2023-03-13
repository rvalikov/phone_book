# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 17th: 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8 Выход
phone_book = []

# def menu(numMenu):
#     switcher = {
#         1: open_phone_book(),
#         2: save_phone_book(),
#         3: show_phone_book(),
#         4: add_phone_book(),
#         5: change_phone_book(),
#         6: search_phone_book(),
#         7: delete_phone_book()
#     }
#     operation = switcher.get(numMenu)

def open_phone_book():
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        global phone_book
        phone_book = data.readlines()

        print('Файл открыт')
        print(phone_book)
        select()


def save_phone_book():
    print("Функция 2 работает")
    with open('phone_book.txt', 'w+', encoding = 'utf-8') as data:
        for i in phone_book:
            data.write(i)
    select()


def show_phone_book():
    print("Функция 3 работает")
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
        for i in phone_book:
            print(' '.join(i.split(';')))
        select()
def add_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
        print("Функция 4 работает")
        user_info = input('Введите данные нового контакта: ')
        phone_book.append(user_info)
    select()
def change_phone_book():
    print("Функция 5 работает")
    user_info = int(input('Введите номер контакта, которого вы хотите изменить: '))
    print("user_info", user_info)
    print(phone_book[user_info])
    new_user_info = input('Введите новые данные контакта: ')
    phone_book[user_info] = new_user_info
    print(phone_book)
    select()

def search_phone_book():
    user_info = int(input('Введите номер контакта, по которому будем искать: '))
    print(phone_book[user_info])
    select()
def delete_phone_book():
    user_info = int(input('Введите номер контакта, которого вы хотите удалить: '))
    print(phone_book[user_info])
    phone_book.pop(user_info)
    print(phone_book)
    select()
def menu(numMenu):
    print("NumMenu = ", numMenu)
    if numMenu == "1":
        print("Вызываю пункт 1")
        open_phone_book()
    else:
        if numMenu == "2":
            print("Вызываю пункт 2")
            save_phone_book()
        else:
            if numMenu == "3":
                print("Вызываю пункт 3")
                show_phone_book()
            else:
                if numMenu == "4":
                    add_phone_book()
                else:
                    if numMenu == "5":
                        change_phone_book()
                    else:
                        if numMenu == "6":
                            search_phone_book()
                        else:
                            if numMenu == "7":
                                delete_phone_book()
def select():
    numMenu = input("Выберите пункт меню\n 1. Открыть файл\n 2. Сохранить файл\n" 
                " 3. Показать контакты\n 4. Добавить контакт\n 5. Изменить контакт\n 6. Найти контакт\n 7. Удалить контакт\nВыбор: ")
    print(numMenu)
    menu(numMenu)
select()