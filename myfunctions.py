from  project import Book
import json

def print_options():
    print("press the specific button")
    print("press 1 to create new book")
    print("press 2 for saving book ")
    print("press 3 for loading books from disk")
    print("press 4 for issue book")
    print("press 5 to update the book")
    print("press  6 to get a single book")


def input_books():
    id = input("ID:")
    name = input("Name:")
    description = input("des :")
    pageno = int(input("pageNO:"))
    author = input("author:")
    issue = input("enter y for yes and n for false")
    issue = (issue == "y" or issue =="Y")

    return {
        'id' : id,
        'name' : name,
        'description' : description,
        'pageno' : pageno,
        'author' : author,
        'issue' : issue,

    }


def create_book():
    print("create the new book")
    book_data=input_books()
    book = Book(book_data['id'], book_data['name'], book_data['description'], book_data['pageno'], book_data['author'], book_data['issue'])
    print(book.dic())

    return book


def savebooks(Book):
    json_books=[]
    for book in Book:
        json_books.append(book.dic)
    try:
        file = open("data.dat","w")
        file.write(json.dumps(json_books, indent=4))

    except:
        print("we have an error")        


