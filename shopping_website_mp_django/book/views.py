from django.shortcuts import render
from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import BookType, Author, Book
from .serializers import BookTypeSerializer, AuthorSerializer, BookSerializer

class AlphabeticalBooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        target_book_type = BookType.objects.filter(Q(name=request.data['book_type_name']))
        target_author = Author.objects.filter(Q(name=request.data['author_name']))
        books = Book.objects.all()
        books.create(
            book_type=target_book_type.first(),
            author=target_author.first(),
            title=request.data['title'],
            price=request.data['price'],
            sypnosis=request.data['sypnosis'],
            image=request.data['book_image'],
            genres=request.data['genres'],
            status=request.data['status'],
            publish_date=request.data['publish_date'],
            publishers=request.data['publishers'],
            is_bestseller=request.data['is_bestseller'],
            number_of_pages=request.data['number_of_pages'],
            slug=request.data['book_slug']
        )
        return Response({"Books": []})

    def delete(self, request, format=None):
        books = Book.objects.all()
        books.filter(
            title=request.data['title']
        ).delete()
        return Response({"Books": []})
    
    def put(self, request, format=None):
        books = Book.objects.all()
        target_book = books.get(
            title=request.data['target_title']
        )
        target_book.book_type=BookType.objects.get(Q(first_name=request.data['book_type_name'])),
        target_book.author=Author.objects.get(Q(first_name=request.data['author_name'])),
        target_book.title=request.data['title'],
        target_book.price=request.data['price'],
        target_book.sypnosis=request.data['sypnosis'],
        target_book.image=request.data['book_image'],
        target_book.genres=request.data['genres'],
        target_book.status=request.data['status'],
        target_book.publish_date=request.data['publish_date'],
        target_book.publishers=request.data['publishers'],
        target_book.is_bestseller=request.data['is_bestseller'],
        target_book.number_of_pages=request.data['number_of_pages'],
        target_book.slug=request.data['book_slug']
        target_book.save()
        return Response({"Books": []})

class AlphabeticalAuthorsList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        authors = Author.objects.all()
        authors.create(
            name=request.data['author_name'],
            country_of_origin=request.data['country_of_origin'],
            image=request.data['author_image'],
            description=request.data['author_description'],
            slug=request.data['author_slug']
        )
        return Response({"Authors": []})

    def delete(self, request, format=None):
        authors = Author.objects.all()
        authors.filter(
            name=request.data['author_name'],
            country_of_origin=request.data['country_of_origin']
        ).delete()
        return Response({"Authors": []})

    def put(self, request, format=None):
        authors = Author.objects.all()
        target_author = authors.get(
            name=request.data['target_author_name'],
            country_of_origin=request.data['target_country_of_origin']
        )
        target_author.name = request.data['author_name']
        target_author.country_of_origin = request.data['country_of_origin']
        target_author.image = request.data['author_image']
        target_author.description = request.data['author_description']
        target_author.slug = request.data['author_slug']
        target_author.save()
        return Response({"Authors": []})

class AlphabeticalBookTypesList(APIView):
    def get(self, request, format=None):
        book_types = BookType.objects.all()
        serializer = BookTypeSerializer(book_types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        book_types = BookType.objects.all()
        book_types.create(
            name=request.data['book_type_name'],
            slug=request.data['book_type_slug']
        )
        return Response({"Authors": []})

    def delete(self, request, format=None):
        book_types = BookType.objects.all()
        book_types.filter(
            name=request.data['book_type_name']
        ).delete()
        return Response({"Authors": []})

    def put(self, request, format=None):
        book_types = BookType.objects.all()
        target_book_type = book_types.get(
            name=request.data['target_book_type_name'],
        )
        target_book_type.name = request.data['book_type_name']
        target_book_type.slug = request.data['book_type_slug']
        target_book_type.save()
        return Response({"Books": []})

class BookDetail(APIView):
    def get_object(self, book_type_slug, author_slug, book_slug):
        try:
            return Book.objects.filter(book_type__slug=book_type_slug).filter(author__slug=author_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, book_type_slug, author_slug, book_slug, format=None):
        book = self.get_object(book_type_slug, author_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class AuthorDetail(APIView):
    def get_object(self, author_slug):
        try:
            return Author.objects.get(slug=author_slug)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, author_slug, format=None):
        author = self.get_object(author_slug)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

class BookTypeDetail(APIView):
    def get_object(self, book_type_slug):
        try:
            return BookType.objects.get(slug=book_type_slug)
        except BookType.DoesNotExist:
            raise Http404

    def get(self, request, book_type_slug, format=None):
        book_type = self.get_object(book_type_slug)
        serializer = BookTypeSerializer(book_type)
        return Response(serializer.data)

@api_view(['POST'])
def book_search(request):
    query = request.data.get('query', '')

    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(sypnosis__icontains=query) | Q(publishers__icontains=query))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({"Books": []})

@api_view(['POST'])
def author_search(request):
    query = request.data.get('query', '')

    if query:
        authors = Author.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    else:
        return Response({"Authors": []})

@api_view(['POST'])
def book_type_search(request):
    query = request.data.get('query', '')

    if query:
        book_types = BookType.objects.filter(Q(name__icontains=query))
        serializer = BookTypeSerializer(book_types, many=True)
        return Response(serializer.data)
    else:
        return Response({"BookTypes": []})