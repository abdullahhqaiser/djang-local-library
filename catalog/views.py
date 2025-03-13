from django.shortcuts import render
from .models import Book, BookInstance, Genre, Author
from django.views import generic


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


class ListBookView(generic.ListView):
    model = Book
    """
    context_object_name : used in template for accessing list of books,
      which is added to context dict 
    
    """
    context_object_name = "book_list"

    """
    template_name : points to html file,which is linked with this view.
    """
    template_name = "books/book_list.html"

    paginate_by = 3

    def get_queryset(self):
        return Book.objects.all()

    # here context mean the data we pass to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verified"] = "yess"

        print(context)
        return context


class BookDetailView(generic.DetailView):
    model = Book

    template_name = "books/book_detail.html"
    context_object_name = "book"


class ListAuthorView(generic.ListView):

    model = Author
    template_name = "authors/author_list.html"
    context_object_name = "authors"

    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "authors/author_detail.html"
    context_object_name = "author"
