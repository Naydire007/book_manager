import pdb

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import author_repository, book_repository


books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/books")
def all_books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods = ["POST"])
def delete_book(id):
    book_repository.delete_book(id)
    return redirect("/books")
# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    return render_template("/books/new.html")
    
# CREATE
# POST '/books'
@books_blueprint.route("/books", methods = ['POST'])
def create_book():
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form [ "publisher"]
    author = request.form [ "author"]
    author = author_repository.select_one(author)
    new_book = Book(title, genre, publisher, author)
    book_repository.save_book(new_book)
    return redirect("/books")

# SHOW
# GET '/books/<id>'



# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'


