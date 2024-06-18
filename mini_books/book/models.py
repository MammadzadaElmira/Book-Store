from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.title}"


class Book(models.Model):
    LANGUAGES = (
        ("AZ", "AZ"),
        ("EN", "EN"),
        ("RU", "RU")
    )

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    published_at = models.PositiveIntegerField()
    language = models.CharField(max_length=4, choices=LANGUAGES)
    page_count = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField(
        null=True, blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
     )

    published_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.title}"
    
    def is_fresh_book(self):
        today = datetime.date.today()
        return self.published_at + datetime.timedelta(days=14) >= today
    
    def get_thumbnail_photo_url(self):
        image_url = self.photos.first()
        if image_url:
            return image_url.img.url
        return ""
    

class BookPhoto(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="photos")
    img = models.ImageField(upload_to="book_photos/%Y/%m/%d/")


    class Meta:
        verbose_name = "Book Photo"
        verbose_name_plural = "Book Photos"
    
    def __str__(self) -> str:
        return f"{self.book.title}"
