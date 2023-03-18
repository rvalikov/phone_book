
class User:
    def __init__(self):
        self.name = input("Введите имя ")
        self.last_name = input("Введите фамилию ")
        self.phone_number = input("Введите телефон ")
    def __repr__(self):
        return f" {self.last_name} {self.name} {self.phone_number}"
def add_phone_book(phone_book):
    # if len(phone_book) == 0:
    #     print('Вы не открыли файл либо файл пуст')
    # else:
    print("Функция 4 работает")
    # user_info = input('Введите данные нового контакта: ')
    # phone_book.append(f"\n{user_info}")


    new_user = User()
    phone_book.append(new_user)
    print("NewUser", new_user)
    for users in phone_book:
        print(users)
    def print_users(phone_book):
        for printsusers in phone_book:
            print("printUsers", printsusers)
    print_users(phone_book)
    return phone_book