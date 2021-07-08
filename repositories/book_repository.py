from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository 

def save_book(book):
    sql = "INSERT INTO books (title, genre, publisher, author_id) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [book.title, book.genre, book.publisher, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id 
    return book

# def select_all():
#     books = []

#     sql = "SELECT * FROM books"
#     results = run_sql(sql)

#     for book in results:
#         title = 
#         genre = 

