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

# CREATE
# POST '/books'



# SHOW
# GET '/books/<id>'

# NEW
# GET '/books/new'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'


