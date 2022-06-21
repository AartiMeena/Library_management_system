class Library:
    def __init__(self, listOfAllBooks):
        self.books = listOfAllBooks

    def displayAllAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrow_book(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 60 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def return_book(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def request_for_book(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def return_book(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Design Patterns","Modern Operating Systems","Computer Graphics","Thining in Java","Programming Ruby","Computer Networks","Database System Concepts",])
    student = Student()
    # centraLibrary.displayAllAvailableBooks()
    while(True):
        Msg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List of all the available books
        2. Request for a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(Msg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAllAvailableBooks()
        elif a == 2:
            centraLibrary.borrow_book(student.request_for_book())
        elif a == 3:
            centraLibrary.return_book(student.return_book())
        elif a == 4:
            print("Thanks for comming!!")
            exit()
        else:
            print("please choose right choice")

        
