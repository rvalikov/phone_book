def show_phone_book(phone_book):
    print("Функция 3 работает")
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
        for elem in phone_book:
            print(elem)
