from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# NEW
# GET '/books/new'

# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'
