from django.db import models

# Модель пользователя
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    membership_type = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

# Модель библиотеки
class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'libraries'
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


    def __str__(self):
        return f"{self.name}, {self.city}"

# Модель автора
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name

# Модель книги
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

# Модель манги
class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    volume = models.IntegerField(blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'manga'
        verbose_name = 'Manga'
        verbose_name_plural = 'Mangas'

    def __str__(self):
        return self.title

# Модель жанра
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'genres'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

# Связь "многие ко многим" между книгами и жанрами
class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_genres'
        verbose_name = 'Book Genre'
        verbose_name_plural = 'Book Genres'

    def __str__(self):
        return f"{self.book.title} - {self.genre.name}"

# Связь "многие ко многим" между мангой и жанрами
class MangaGenre(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'manga_genres'
        verbose_name = 'Manga Genre'
        verbose_name_plural = 'Manga Genres'

    def __str__(self):
        return f"{self.manga.title} - {self.genre.name}"

# Модель для хранения копий книг и манги в разных библиотеках
class Copy(models.Model):
    ITEM_TYPE_CHOICES = [
        ('book', 'Book'),
        ('manga', 'Manga'),
    ]

    item_id = models.IntegerField()  # ID книги или манги
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)  # Тип элемента
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    class Meta:
        db_table = 'copies'
        verbose_name = 'Copy'
        verbose_name_plural = 'Copys'

    def __str__(self):
        return f"{self.get_item_type_display()} ID {self.item_id} in {self.library.name}"

# Модель бронирования книг и манги
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        db_table = 'reservations'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f"Reservation by {self.user.name} for {self.copy}"

# Модель отзывов пользователей о книгах и манге
class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.IntegerField()  # ID книги или манги
    item_type = models.CharField(max_length=10, choices=Copy.ITEM_TYPE_CHOICES)  # Тип элемента
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Review by {self.user.name} on {self.get_item_type_display()} ID {self.item_id}"
