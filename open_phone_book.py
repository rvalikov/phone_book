def open_phone_book(phone_book):
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        phone_book = list(data.readlines())
        print('Файл открыт')
        print(phone_book)
    return phone_book
