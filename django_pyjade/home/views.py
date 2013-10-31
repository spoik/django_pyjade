from django.views.generic.list import ListView

from .models import Book

class BookListView(ListView):
    model = Book
    queryset = Book.objects.order_by("name")
    template_name = 'home/book_list.jade'
