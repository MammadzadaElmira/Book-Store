from django.shortcuts import render

# Create your views here.
from .models import Genre, Book

def home(request):
    books = Book.objects.all()
    context = {
        "BOOKS": books
    }
    return render(request, "book/book_cover.html", context)