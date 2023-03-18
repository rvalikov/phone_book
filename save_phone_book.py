import pickle
def save_phone_book(phone_book):
    print("Функция 2 работает")
    with open('phone_book.pickle', 'wb') as data:
        pickle.dump(phone_book, data)
        # for i in phone_book:
        #     print("i= ", i)
        #
        #     print("ijson= ", i)
        #     data.write(i)
