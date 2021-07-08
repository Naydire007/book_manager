import pdb
from models.book import Book
from models.author import Author
from repositories import book_repository
from repositories import author_repository

author_1 = Author("Roddy", "Doyle")
author_2 = Author(" J. R. R.", "Tolkien")
author_3 = Author("Fyodor", "Dostoyevsky")

book_1 = Book("Paddy Clarke Ha Ha Ha", "Fiction", "Minerva", author_1)
book_2 = Book("The Silmarillion", "Fantasy", "Unwin Paperbacks", author_2)
book_3 = Book("Brothers Karamazaov", "Fiction", "Penguin", author_3)

author_repository.save_author(author_1)
author_repository.save_author(author_2)
author_repository.save_author(author_3)

book_repository.save_book(book_1)
book_repository.save_book(book_2)
book_repository.save_book(book_3)
