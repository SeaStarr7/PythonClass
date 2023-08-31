# Week 8: Library Part Two
# 
# On week 6 we made a program for a library that catalogs books in a library. However you might've 
# noticed that the catalog is reset every time we run the program. We can fix this with file 
# reading and writing. 
# 
# Write a function called openFile, this function will take no parameters.
# In the function open catalog.txt in read and write mode, then return the opened file.
# 
# Write a function called intializeDict, this function will take one parameter a file and return a list of dictionaries.
# First initalize the dictionary you'll be returning. Then loop over every line in the file, To do this use the readlines() method. 
# Once you've gotten a line from the file, use the split method to 
# 
# ------------------------------------------------------------------------------------------------------------------------------------


def openFile():
    file = open("catalog.txt", "w+")
    return file

def intializeDict(file):
    a_list = []
    
    for line in file.readlines():
        line.split(',')
        adict["title"] = line[0]
        adict['isbn'] = line[1]
        adict["genre"] = line[2]
        a_list.append(adict)
    return adict



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
            break
        else:
            print("Answer not recognised, please try again")


def writeToFile(a_list_of_dictionaries, file):
    for book in a_list_of_dictionaries:
        line = str(book['title'] + "," + book['isbn'] + "," + book['genre'])
        file.write(line)


file = openFile()
adict = intializeDict(file)
libInterface(adict)
writeToFile(adict, file)





