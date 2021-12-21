"""
For anyone working on this project, the code's very messy and not documented well. It's broken at various parts
and I've used some crapy ways to make it work, still, it dosen't work as you'd expect an LMS to work. if you can just document it
or give opinion as comments(python one's) it'd be appreciated. AND if your working locally and not on cloud- name the files as 
they are named here and keep all the files in the same folder or code will get fucked up, THANKS. 
"""

import csv


class Library:
    def __init__(self, book_dict, lender_dict, name):
        self.book_dict = book_dict
        self.name = name
        self.lender_dict = lender_dict

    def display_books(self):
        print("We have following books in our Library : ")
        book_no = 0
        for book in self.book_dict.items():
            book_no += 1
            print(str(book_no) + ". ", "  by  ".join(book).title())

    def lend_book(self, lender, book):
        if book not in self.lender_dict.keys():
            with open("lenders.csv", "a") as f:
                f.write("\n" + book + "," + lender)
                print("Lender database has been updated.")
        else:
            print("The book is already being used by {0}.".format(
                self.lender_dict[book]))

    def add_book(self, book, author):
        with open("books.csv", "a") as f:
            f.write("\n" + book + "," + author)
        print("The book has been added to the book list.")

    def return_book(self, book):
        self.lender_dict.pop(book)

    def find_book_by_name(self, book):
        if book in self.book_dict.keys():
            print("Yes, " + book.title() + " is in the Library")
        else:
            print("The book is not in the Library.")

    def find_book_by_author(self, author):
        if author in self.book_dict.values():
            author_key = [book for book,
                          name in self.book_dict.items() if name == author]
            print("Yes, we have", " ".join(author_key).title(),
                  "by", author.title() + ".")
        else:
            print("We dont have books by this author.")


book_dict = {}
with open("books.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        book_dict.update({row["book"]: row["author"]})

lender_dict = {}
with open("lenders.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        lender_dict.update({row["book"]: row["lender"]})

name_of_library = input("Enter the name of your library : ").strip()
library = Library(book_dict, lender_dict, name_of_library)

while True:
    print("Welcome to {}, Enter your choice to continue : ".format(library.name))
    print("1. Display books ")
    print("2. Lend a book ")
    print("3. Add a book ")
    print("4. Return a book ")
    print("5. Find a book")
    user_choice = input("Enter your choice : ").strip()
    if user_choice not in ["1", "2", "3", "4", "5", "c", "q"]:
        print("Please enter a valid input.")
        continue
    elif user_choice in ["1", "2", "3", "4", "5"]:
        user_choice = int(user_choice)
    if user_choice == 1:
        library.display_books()
    elif user_choice == 2:
        book = input(
            "Enter the name of the book which the user wants to lend : ").lower().strip()
        user = input(
            "Enter the name of the person who wants to lend the book : ").lower().strip()
        library.lend_book(user, book)
    elif user_choice == 3:
        book = input(
            "Enter the name of the book you want to add : ").lower().strip()
        author = input(
            "Enter the name of the author of the book : ").lower().strip()
        library.add_book(book, author)
    elif user_choice == 4:
        book = input("Enter the book user wants to return : ").lower().strip()
        library.return_book(book)
    elif user_choice == 5:
        while True:
            print("1. Find by book name")
            print("2. Find by author name")
            user_choice_3 = input("Enter your choice : ")
            if user_choice_3 not in ["1", "2"]:
                print("Please enter a valid input.")
                continue

            else:
                if int(user_choice_3) == 1:
                    book = input(
                        "Enter the name of the book you want to find : ").lower().strip()
                    library.find_book_by_name(book)
                    break
                elif int(user_choice_3) == 2:
                    author = input(
                        "Enter the name of author you want to find book of : ").lower().strip()
                    library.find_book_by_author(author)
                    break

    elif user_choice in ["q", "c"]:
        if user_choice == "q":
            exit()
        else:
            continue

    user_choice2 = ""
    while user_choice2 != "c" and user_choice2 != "q":
        user_choice2 = input(
            "Press 'q' to Quit or 'c' to Continue : ").lower().strip()
        print("\n")
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            with open("books.csv", "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    book_dict.update({row["book"]: row["author"]})
            with open("lenders.csv", "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    lender_dict.update({row["book"]: row["lender"]})
            continue
