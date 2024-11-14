from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path('authors/', views.authors_list, name='authors'),
    path('books/', views.books_list, name='books'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('libraries/', views.libraries, name='libraries'),
]
