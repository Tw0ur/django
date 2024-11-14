from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

from .models import Book


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после регистрации
            return redirect("home")  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()
    return render(request, "library/register.html", {"form": form})
def home(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {"books": books})

def authors_list(request):
    return render(request, 'library/authors.html')

def books_list(request):
    return render(request, 'library/books.html')

def book_detail(request, isbn):
    book = Book.objects.get(isbn=isbn)
    return render(request, 'library/book_detail.html', {"book": book})
def libraries(request):
    return render(request, 'library/libraries.html')
