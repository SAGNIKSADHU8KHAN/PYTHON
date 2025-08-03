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

        