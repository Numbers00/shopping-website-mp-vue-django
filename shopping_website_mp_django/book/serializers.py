from rest_framework import serializers

from .models import BookType, Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'price',
            'sypnosis',
            'image',
            'genres',
            'status',
            'publish_date',
            'publishers',
            'is_bestseller',
            'number_of_pages',
            'get_absolute_url'
        )

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
        
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'country_of_origin',
            'image',
            'description',
            'get_absolute_url',
            'books'
        )

class BookTypeSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
        
    class Meta:
        model = BookType
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'books'
        )