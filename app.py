import myfunctions
import os
myfunctions.print_options()
option = input()
book=[]
while option !='X' and option != "x":
    if option == '1' :
        book.append(myfunctions.create_book())

    elif option == '2' :
        myfunctions.savebooks(book)
    os.system("cls")    
    myfunctions.print_options()
    option = input()        
    