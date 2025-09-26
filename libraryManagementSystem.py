class LibraryItem:
     #constructor
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=True

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def check_out(self):
        if self.available:
            print(f"Checked out: {self}")
            self.available=False
        else:
            print(f"{self} is not available for checkout!")
    def check_in(self):
        print(f"Checked in : {self}")
        self.available=True
        
#child class of libray item
#inheritance
class Book(LibraryItem):
    def __init__(self, title, author, isbn,genre):
        super().__init__(title, author, isbn)
        self.genre=genre
    def __str__(self):
        return f"{super().__str__()} (Genre: {self.genre})"

class User:
    def __init__(self,name):
        self.name=name
    def borrow_item(self,item):
        item.check_out()
    def return_item(self,item):
        item.check_in()



library = []
book1=Book("Make up your Mind","Uzair Hassan","2001256","generation")
library.append(book1)

user1=User("Hassan")
user2=User("Asif")
user1.borrow_item(book1)
user2.borrow_item(book1)

print("Library item :")
for item in library:
   print(item)