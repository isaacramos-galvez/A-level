class stock_item:
    def __init__(self, title, on_loan, date_acquired):
        self.title = title
        self.on_loan = on_loan
        self.date_acquired = date_acquired

class library_book(stock_item):
    def __init__(self, author, ISBN, on_loan, date_acquired, title):
        self.author = author
        self.ISBN = ISBN
        super().__init__(title, on_loan, date_acquired)

    def book_details(self):
        print(f"[",self.author,"][",self.title,"][",self.ISBN,"][",self.on_loan,"][",self.date_acquired,"]")

    def return_book(self):
        self.on_loan = False
        return self.on_loan
    
    def take_out_book(self):
        self.on_loan = True
        return self.on_loan

class CD(stock_item):
    def __init__(self, artist, playing_time, on_loan, date_acquired, title):
        self.artist = artist
        self.playing_time = playing_time
        super().__init__(on_loan, date_acquired, title)

    def CD_details(self):
        print(f"[",self.artist,"][",self.title,"][",self.playing_time,"][",self.on_loan,"][",self.date_acquired,"]")

    def return_CD(self):
        self.on_loan = False
        return self.on_loan

    def take_out_CD(self):
        self.on_loan = True
        return self.on_loan

def test_library():
    book1 = library_book('William Shakespeare', '123456789', 'False', '1-1-2024', 'Hamlet')
    CD1 = CD('Michael Jackson', '3.81', 'True', '1-2-2013','Another Part of Me')
    items = [book1, CD1]
    for item in items:
        item.book_details()
        item.CD_details()
    out_book = input("Do you want to take out a book")
    if out_book == "yes":
        take_out_book()
    else:
        self.onloan = False
    out_CD = input("Do you want to take out a CD")
    if out_CD == "yes":
        take_out_CD()
    else:
        self.onloan = False
    return_item = input("Do you have any items to return?")
    if return_item == "yes":
        which_item = input("Do you want ot return a book or a CD?")
        if which_item == "book":
            return_book()
        elif which_item == "CD":
            return_CD()
    
test_library()



    