# 
# Your local library has hired you to write a computer program to organize and catalog the books in the library. To do this 
# we're going to use a list of dictionaries!
# 
# 
# First let's write a function called addBook, this function will take a list of dictionaries and return nothing. 
# Ask the user for the title of the book, the ISBN number of the book, and the genre. 
# Add the information to a dictionary, where the keys are the title, ISBN and genre, and the values are the user's input.
# Finally append your dictionary to the list of books.
#
# 
# Write a function called findByTitle, this function will take a list of books and return nothing.
# Ask the user for the title of their desired book, then loop though the books in the list to find a matching title.
# If the book is found print the book's information, otherwise print "Book not found"
# 
# 
# Write a function called searchGenre, this function will take a list of books and return nothing.
# Ask the user for their desired genre, then loop though the books in the list and print all books
# with that genre.
# 
# 
# Write a function called checkOut, this will take a list of books and return nothing.
# Ask the user for the ISBN of their desired book, then loop though the books in the list to find a matching title.
# If the book is found print "(Book_title) successfully checked out" then, remove it from the list of books.
# Otherwise print "Book not found"
#
# 
# Write a function called libInterface, this will take a list of books, and return nothing.
# Ask the user if they'd like to add a book[A], find a book by title[T], search genres[G], checkout a book[C] or quit[Q]
# If the user inputs 'A' then call addBook
# If the user inputs 'T' then call findByTitle
# If the user inputs 'G' then call searchGenre
# If the user inputs 'C' then call checkOut
# If the user inputs 'Q' then end the program
# If the user did not enter any of these options ask them to try again
# 
# 
# Write a function called main, this will take no parameters and return nothing. 
# call libInterface and pass in an empty list
# 
# Extra: What if you want to see every book the library has? Try writing a function to print them all out!
# 
# --------------------------------------------------------------------------------------------------------------------------




def addBook(a_list_of_dictionaries):
    book = {}
    book_title = input("title: ")
    book_isbn = input("isbn: ")
    book_genre = input("genre: ")
    book["title"] = book_title
    book["isbn"] = book_isbn
    book['genre'] = book_genre
    a_list_of_dictionaries.append(book)
    

def findByTitle(a_list_of_dictionaries):
    desired_book = input("What book do you want: ")
    for book in a_list_of_dictionaries:
        if book["title"] == desired_book:
            print(book)
            return
    print("book not found")

def searchGenre(a_list_of_dictionaries):
    desired_genre = input("What genre do you want: ")
    for book in a_list_of_dictionaries:
        if book["title"] == desired_genre:
            print(book)
    print("no books found")


def checkOut(a_list_of_dictionaries):
    isbn = input("Enter ISBN: ")
    for book in a_list_of_dictionaries:
        if book["isbn"] == isbn:
            print(book["title"], "checked out.")
            a_list_of_dictionaries.remove(book)
            return
    print("no books found")

def libInterface(a_list_of_dictionaries):
    while True:
        print("What would you like to do?")
        print("addBook [A]")
        print("findTitle[T]")
        print("searchGenre[G]")
        print("checkOut[C]")
        print("Quit[Q]")
        choice = input()
        if choice == "A":
            addBook(a_list_of_dictionaries)
        elif choice == "T":
            findByTitle(a_list_of_dictionaries)
        elif choice == "G":
            searchGenre(a_list_of_dictionaries)
        elif choice == "C":
            checkOut(a_list_of_dictionaries)
        elif choice == "Q":
            quit
        else:
            print("Answer not recognised, please try again")


thing = []
libInterface(thing)




