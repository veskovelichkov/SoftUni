def add_book(shelf, book_name):
    if book_name not in shelf:
        shelf.insert(0, book_name)
    return shelf


def take_book(shelf, book_name):
    if book_name in shelf:
        shelf.remove(book_name)
    return shelf


def insert_book(shelf, book_name):
    if book_name not in shelf:
        shelf.append(book_name)
    return shelf


def check_book(shelf, index):
    if index in range(len(shelf)):
        print(shelf[index])


def swap_books(shelf, first_book, second_book):
    if first_book in shelf and second_book in shelf:
        first_book_index, second_book_index = shelf.index(first_book), shelf.index(second_book)
        shelf[first_book_index], shelf[second_book_index] = shelf[second_book_index], shelf[first_book_index]
    return shelf


books = input().split("&")
command = input()
while True:
    if command == "Done":
        break
    command_split = command.split(" | ")
    event = command_split[0]
    book_or_index = command_split[1]
    if event == "Add Book":
        books = add_book(books, book_or_index)
    if event == "Take Book":
        books = take_book(books, book_or_index)
    if event == "Swap Books":
        second_book = command_split[2]
        books = swap_books(books, book_or_index, second_book)
    if event == "Insert Book":
        books = insert_book(books, book_or_index)
    if event == "Check Book":
        book_or_index = int(book_or_index)
        check_book(books, book_or_index)
    command = input()
print(", ".join(books))