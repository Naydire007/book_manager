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

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    
    for row in results:
        author = author_repository.select_one(row['author_id'])
        book = Book(row['title'],row['genre'],row['publisher'], author, row['id'])
        books.append(book)
    return books

def select_book(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select_one(result['author_id'])
        book = Book(result['title'],result['genre'],result['publisher'], author, result['id'])
    return book

def delete_book(id):

    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)