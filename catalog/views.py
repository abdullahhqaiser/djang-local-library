from django.shortcuts import render
from .models import Book, BookInstance, Genre, Author


def index(request):
    """
    1 - grabs data from model.
    2 - create context dict
    3 - send context with page that created in templates directory

    """

    book_count = Book.objects.count()
    instances_count = BookInstance.objects.count()

    num_instances = BookInstance.objects.count()
    num_authors = Author.objects.count()

    context = {
        "book_count": book_count,
        "instance_count": instances_count,
        "num_instance_avaliable": num_instances,
        "num_author": num_authors,
    }

    return render(request, "index.html", context=context)
