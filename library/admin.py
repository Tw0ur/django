from django.contrib import admin
from .models import User, Library, Author, Book, Manga, Genre, BookGenre, MangaGenre, Copy, Reservation, Review

# Модель User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'membership_type', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('membership_type',)

# Модель Library
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone')
    search_fields = ('name', 'city')

# Модель Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Модель Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_year', 'language')
    search_fields = ('title', 'isbn')
    list_filter = ('publication_year', 'language')

# Модель Manga
@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'volume', 'chapter', 'publication_year', 'language')
    search_fields = ('title',)
    list_filter = ('publication_year', 'language')

# Модель Genre
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Модель BookGenre
@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('book', 'genre')
    search_fields = ('book__title', 'genre__name')

# Модель MangaGenre
@admin.register(MangaGenre)
class MangaGenreAdmin(admin.ModelAdmin):
    list_display = ('manga', 'genre')
    search_fields = ('manga__title', 'genre__name')

# Модель Copy
@admin.register(Copy)
class CopyAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_type', 'library', 'available')
    list_filter = ('item_type', 'library', 'available')
    search_fields = ('item_id',)

# Модель Reservation
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'copy', 'reservation_date', 'due_date', 'status')
    list_filter = ('status',)
    search_fields = ('user__name', 'copy__item_id')

# Модель Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_id', 'item_type', 'rating', 'created_at')
    list_filter = ('item_type', 'rating')
    search_fields = ('user__name', 'item_id')
