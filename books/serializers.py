from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'average_rating', 'language_code',
                  'num_pages','ratings_count','text_reviews_count','publication_date','publisher')
