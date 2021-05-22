import myfunctions
import os
myfunctions.print_options()
option = input()
book=[]
while option !='X' and option != "x":
     if option == '1' :
        books.append(myfunctions.create_book())
    elif option == '2' :
        myfunctions.savebooks(books)
        print("gg")

    elif option=='3':
       books =myfunctions.load_books()
    elif option==4 :
        myfunctions.issue_book(books) 
    elif option==5 :
        myfunctions.return_book(books)
    elif option==6 :
        myfunctions.update_book(books)
    elif option==7 :
        myfunctions.show_allbooks(books)
    elif option==8 :
        myfunctions.show_book(books)

    else:
        print("exist")
    os.system("cls")    
    myfunctions.print_options()
    option = input()        
    
