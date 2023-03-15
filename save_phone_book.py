def save_phone_book(phone_book):
    print("Функция 2 работает")
    with open('phone_book.txt', 'w+', encoding = 'utf-8') as data:
        for i in phone_book:
            data.write(i)
