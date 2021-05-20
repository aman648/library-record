class Book:
    def __init__(self, id,name, desciption, pageno, author, issue):
        self.id = id
        self.name = name
        self.description = desciption
        self.pageno = pageno
        self.author = author
        self.issue  = issue


    def dic(self):
       dictionary = {
           "id": self.id,
           "name": self.name,
           "description" : self.description,
           "pageno" : self.pageno,
           "author" : self.author,
           "issue"  : self.issue,
        
       }
       return dictionary 

       


