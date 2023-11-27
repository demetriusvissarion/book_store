from lib.book import Book

class BookRepository:
    def __init__(self, connection=None):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books

    def add(self, book):
        self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [book.title, book.author_name])
        return None