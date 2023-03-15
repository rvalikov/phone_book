def change_phone_book(phone_book):
    print("Функция 5 работает")
    user_info = int(input('Введите номер контакта, которого вы хотите изменить: '))
    print("user_info", user_info)
    print(phone_book[user_info])
    new_user_info = input('Введите новые данные контакта: ')
    phone_book[user_info] = f"\n{new_user_info}"
    print(phone_book)
    return phone_book
