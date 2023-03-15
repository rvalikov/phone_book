def add_phone_book(phone_book):
    # if len(phone_book) == 0:
    #     print('Вы не открыли файл либо файл пуст')
    # else:
    print("Функция 4 работает")
    user_info = input('Введите данные нового контакта: ')
    phone_book.append(f"\n{user_info}")
    return phone_book