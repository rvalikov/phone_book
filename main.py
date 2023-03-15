# Сделал с архитектурой, куда здесь прилепить класс, не понял
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
import add_phone_book
import show_phone_book
import open_phone_book
import save_phone_book
import change_phone_book
import search_phone_book
import delete_phone_book
import select
phone_book = []

class User:
    def __init__(self, name: str, last_name: str,phone_number: str):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
    def __str__(self):
        return f"Пользователь {self.last_name}, {self.name}, телефон{self.phone_number}"


def menu(nummenu):
    print(nummenu)
    global phone_book
    match nummenu:
        case "1":
            phone_book = open_phone_book.open_phone_book(phone_book)
            nummenu=select.select()
            menu(nummenu)
        case "2":
            print("Вызываю пункт 2")
            save_phone_book.save_phone_book(phone_book)
            nummenu = select.select()
            menu(nummenu)
        case "3":
            print("Вызываю пункт 3")
            show_phone_book.show_phone_book(phone_book)
            nummenu = select.select()
            menu(nummenu)
        case "4":
            print("Вызываю пункт 4")
            add_phone_book.add_phone_book(phone_book)
            nummenu = select.select()
            menu(nummenu)
        case "5":
            print("Вызываю пункт 5")
            change_phone_book.change_phone_book(phone_book)
            nummenu = select.select()
            menu(nummenu)
        case "6":
            print("Вызываю пункт 6")
            search_phone_book.search_phone_book(phone_book)
            nummenu = select.select()
            menu(nummenu)
        case "7":
            print("Вызываю пункт 7")
            delete_phone_book.delete_phone_book(phone_book)
            nummenu = select.select()
            menu(nummenu)


ivanov = User("Иван", "Иванов", "11111111111")
print("ivanov= ", ivanov)
nummenu=select.select()
menu(nummenu)