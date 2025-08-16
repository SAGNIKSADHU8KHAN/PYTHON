class Library:

    def __init__(self,list,name):

        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f" We have the following books in our library : {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):

        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The len book database has been updated, you can now take the book")

        else:
            print(f" The book is taken by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print(f" {book} has been added to the booklist. ")


    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':

    books = Library(["Rich Dad Poor Dad, Harry Potter, The housemaid, A man called Ove, A thousand splendid suns, The kite runner, The forest of enchantments, The palace of illusions"], "Let's Upskill")

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue")

        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()

        elif user_choice ==2:

            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add :")
            books.addBook(book)

        elif user_choice == 4:
            book = ("Enter the name of the book you want return :")
            books.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""

        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
            
            

         

        