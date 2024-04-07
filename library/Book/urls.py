from django.urls import path
from .views import *

urlpatterns = [
    # all books
    path('books/', getBook, name='book'),
    # book by id
    path('books/<str:pk>', getBookByID, name='book_id'),
    # add book
    path('books/add/', add_book, name='add_book'),
    # update book
    path('books/update/<str:pk>/', update_book, name='update_book'),
    # delete book
    path('books/delete/<str:pk>/', delete_book, name='delete_book'),
    # get students
    path('students/', getStudent, name='student'),
    # get profs
    path('profs/', getProf, name='prof'),
    # get rented books
    path('rentbooks/', getRentBook, name='rent_book'),
]
