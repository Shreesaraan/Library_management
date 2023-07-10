class LibraryItem:
    def __init__(self,id,title,year):
        self.id = id
        self.__title = title
        self.year = year

    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.__title
    
    def get_year(self):
        return self.year
    
    
class Book(LibraryItem):
    def __init__(self, id, title, year,author):
        super().__init__(id, title, year)
        self.author = author

    def get_author(self):
        return self.author

class Magazine(LibraryItem):
    def __init__(self, id, title, year,issue):
        super().__init__(id, title, year)
        self.issue = issue

    def get_issue(self):
        return self.issue


book1=Book(1,"The Murder in the Orient Express",1934,"Agatha Christie")
print("Book Details:")
print("ID: ",book1.get_id())
print("Title: ",book1.get_title())
print("Year: ",book1.get_year())
print("Author: ",book1.get_author())

magazine1=Magazine(1,"Kerala Crime Files",2023,"Magazine not Found")
print("Magazine Details:")
print("ID: ",magazine1.get_id())
print("Title: ",magazine1.get_title())
print("Year: ",magazine1.get_year())
print("Author: ",magazine1.get_issue())