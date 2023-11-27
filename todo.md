### Design Recipe

The code for `Artist` and `ArtistRepository` classes was created following this [Design
Recipe](../resources/repository_class_recipe_template.md) to design, test-drive and
implement them for a table. The outline for the recipe is:

  1. Design and create the table if needed.
  2. Create test SQL seeds.
  3. Define the Model and Repository class names. = book & book_repository

  4. Implement the Model class.
  5. Design the Repository class interface.
  6. Write test examples.
  7. Test-drive and implement the Repository class behaviour.


## Challenge
Your assignment is to use the design recipe above to design, then test-drive a
`Book` class and a `BookRepository` class with an `all` method.

> __Note__
> Follow the steps below, those in the starter project and design recipe
> carefully!

1. Set up a new project called `book_store` from the
   [starter](https://github.com/makersacademy/databases-in-python-project-starter).
2. Use the `book_store` SQL seed instead of the `music_library` seed. You can
   find this in the `seeds` directory in the starter.
3. Follow the design recipe as usual, before starting to test-drive the classes.
4. Once you've done the design recipe, start recording yourself.
5. Test-drive a `Book` class that has attributes for each column in the `books`
   table, using the example(s) from your design.
6. Test-drive a `BookRepository` class that has a method `all` that returns a
   list of `Book` objects.

   
7. Write a small program in `app.py` using the class `BookRepository` to print
   out the list of books to the terminal.

You should get an output that looks roughly like this:

```shell
# In the project directory book_store

; pipenv shell
; python app.py

1 - Nineteen Eighty-Four - George Orwell
2 - Mrs Dalloway - Virginia Woolf
3 - Emma - Jane Austen
4 - Dracula - Bram Stoker
5 - The Age of Innocence - Edith Wharton
```