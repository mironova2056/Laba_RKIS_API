from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    biography = models.TextField(blank=True)
    def __str__(self):
        return self.name
class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-fiction'),
        ('textbook', 'Textbook'),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year_publication = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/')
    book_file = models.FileField(upload_to='saved_books/', blank=True, null=True)
    class Meta:
        unique_together = ('title', 'author', 'year_publication', 'publisher')
    def __str__(self):
        return self.title
