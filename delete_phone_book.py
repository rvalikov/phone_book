def delete_phone_book(phone_book):
    user_info = int(input('Введите номер контакта, которого вы хотите удалить: '))
    print(phone_book[user_info])
    phone_book.pop(user_info)
    print(phone_book)
    return phone_book