import datetime
import random

LIBRARY = []


def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


class Author:
    def __init__(self, first_name, last_name, notes):
        self.id = uniqueid()
        self.validation(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.notes = notes
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.books = []

    def __add__(self, other):
        self.books.append(other.view_book())


    def author_books(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "notes": self.notes,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "books": self.books

        }

    def validation(self, first_name='', last_name=''):
        if first_name != '' or last_name != '':
            if len(first_name) > 45:
                raise Exception("Exceeded the maximum length : ", first_name)
            elif len(last_name) > 45:
                raise Exception("Exceeded the maximum length : ", last_name)
        else:
            raise Exception("please fill all the field")


class Books:

    def __init__(self, title):
        self.validation(title)
        self.id = uniqueid()
        self.title = title
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def view_book(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def validation(self, title=''):
        if title == '' or len(title) > 255:
            raise Exception("Exceeded the maximum length : ", title)


class Main:
    temp_author = None
    temp_book = None

    def __init__(self):
        while True:
            beg = input(
                'what do you want to do? answer with (1,2,3)\n 1- Add new author \n 2- Edit library data \n 3- show the collection \n')
            if beg == '1':
                self.add_author()
                print(self.temp_author.author_books())
                LIBRARY.append(self.temp_author)
            elif beg == '2':
                self.get_author()
                while True:
                    sec_answer = input(
                        'what do you want to do? answer with (1,2)\n 1- Add new book \n 2- Edit author info \n 3- Edit book data \n 4- Delete book \n 5- Delete user \n')

                    if sec_answer == '1':  # DONE + TESTED
                        self.add_book(self.temp_author)
                    elif sec_answer == '2':  # DONE + TESTED
                        self.update_author_info()
                    elif sec_answer == '3':  # DONE + TESTED
                        self.update_book_info()

                    elif sec_answer == '4':  # DONE + TESTED
                        self.delete_book()

                    elif sec_answer == '5':  # DONE + TESTED
                        self.delete_author()
                    else:
                        print('please enter valid answer')

            elif beg == '3':
                for author in LIBRARY:
                    print(vars(author))

            else:
                print('please enter valid answer')  # change latter
                break
            self.clear_var()
    def delete_author(self):
        LIBRARY.remove(self.temp_author)
        print('DELETED')

    def update_author_info(self):
        author = self.temp_author

        is_exist = False
        while is_exist == False:
            fname = input("please enter first name : ")
            lname = input("please enter last name : ")
            note = input("please enter note about the author : ")
            is_exist = self.author_validation(fname, lname)
            author.first_name = fname
            author.last_name = lname
            author.notes = note
            author.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('UPDATED')

            if is_exist == False:
                print("BOOK DOESN'T EXIST")
            return

    def update_book_info(self):  # TODO create method that get book title | update date on the LIBRARY
        books = self.temp_author.books
        is_exist = False
        while is_exist == False:
            book_title = input("please enter book's title : ")
            for book in books:
                print(book)
                if book_title == book["title"]:
                    is_valid = False
                    while not is_valid:
                        new_title = input('please enter the new title : ')
                        is_valid = self.book_validation(new_title)
                        book["title"] = new_title
                        book["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print('UPDATED\n', book)
                    is_exist = True
                    break
            if is_exist == False:
                print("BOOK DOESN'T EXIST")
            return

    def book_validation(self, title=''):
        if title == '' or len(title) > 255:
            return False
        return True

    def author_validation(self, first_name='', last_name=''):
        if first_name != '' or last_name != '':
            if len(first_name) > 45:
                print("invalid first name length")
                return False
            elif len(last_name) > 45:
                print("invalid last name length")
                return False
        else:
            print("please fill all the field")
            return False
        return True

    def clear_var(self):
        self.temp_author = None
        self.temp_book = None

    def delete_book(self):

        books = self.temp_author.books
        is_exist = False
        while is_exist == False:
            book_title = input("please enter book's title : ")
            for book in books:
                if book_title == book["title"]:
                    books.remove(book)
                    print('DELETED')
                    is_exist = True
                    break
            if is_exist == False:
                print("BOOK DOESN'T EXIST")
            return

    def get_author(self):
        is_exist = False
        while is_exist == False:
            author_name = input('please enter author full name : ')
            for author in LIBRARY:
                name = author.first_name + ' ' + author.last_name
                if author_name == name:
                    print('MATCHED')
                    self.temp_author = author
                    is_exist = True
                    break
            if is_exist == False:
                print("USER DOESN'T EXIST")  # change latter

    def get_book(self):
        is_exist = False
        books = self.temp_author.books
        while is_exist == False:
            book_title = input("please enter book's title : ")
            for book in books:
                print(book)
                if book_title == book["title"]:
                    print('MATCHED')
                    self.temp_book = book
                    is_exist = True
                    break
            if is_exist == False:
                print("BOOK DOESN'T EXIST")
            return

    def add_author(self):
        fname = input('Enter author first name : ')
        lname = input('Enter author last name : ')
        notes = input('(optional) Enter note about the author : ')
        self.temp_author = Author(fname, lname, notes)

        temp_loop = True
        while temp_loop:
            hasBooks = input(
                'Does your author has any books ?(y,n) ' if self.temp_book == None else 'Do you want to add another book ? (y,n)')
            if hasBooks == 'n':
                return
            elif hasBooks != 'y':
                print('please Enter valid value')
            else:
                self.add_book(self.temp_author)

    def add_book(self, author):
        title = input("Enter book's title : ")
        self.temp_book = Books(title)
        self.add_book_to_author(author, self.temp_book)

    def add_book_to_author(self, author, book):
        author + book


Main()
