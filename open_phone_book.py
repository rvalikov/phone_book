import json
import add_phone_book
# def open_phone_book(phone_book):
#     with open('phone_book.txt', 'r', encoding='utf-8') as data:
#         phone_book = list(data.readlines())
#
#         print('Файл открыт')
#         if len(phone_book) == 0:
#             print("Файл пустой, введите первого пользователя")
#             add_phone_book.add_phone_book(phone_book)
#         print(phone_book)
#     return phone_book
import pickle

def open_phone_book(phone_book):
    class Person:
        def __init__(self, name, phone):
            self.name = name
            self.phone = phone

        def __repr__(self):
            return f"Person(name='{self.name}', phone='{self.phone}')"


    # чтение массива объектов из файла
    with open('phone_book.pickle', 'rb') as data:
        phone_book = pickle.load(data)

    print("Phone book пункт 1", phone_book)
    print(type (phone_book))
    return phone_book
