from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.ListBookView.as_view(), name="books"),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    # authors urls
    path("authors/", views.ListAuthorView.as_view(), name="authors"),
    path("authors/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
]
