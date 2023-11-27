from lib.book import Book


"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == "Nineteen Eighty-Four"
    assert book.author_name == "George Orwell"


