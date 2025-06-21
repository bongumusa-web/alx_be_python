class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author =  author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        self.file_size = file_size
        super().__init__(title,author)

    def __str__(self):
        return f"{self.title} by {self.author}, File size: {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        self.page_count = page_count
        super().__init__(title,author)

    def __str__(self):
        return f"{self.title} by {self.author}, Page count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []



    def add_book(self, book):
        self.books.append(book)
        return self.books

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")

