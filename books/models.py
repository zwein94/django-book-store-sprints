from django.db import models


class Book(models.Model):

    title = models.TextField(default='')
    authors = models.TextField(default='')
    average_rating = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    language_code = models.CharField(max_length=70, blank=False, default='')
    num_pages = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    ratings_count = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    text_reviews_count = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    publication_date = models.CharField(max_length=150, blank=True, default='')
    publisher = models.TextField(default='')