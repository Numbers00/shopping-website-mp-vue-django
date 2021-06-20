from django.urls import path, include

from book import views

urlpatterns = [
    path('alphabetical-books/', views.AlphabeticalBooksList.as_view()),
    path('alphabetical-authors/', views.AlphabeticalAuthorsList.as_view()),
    path('alphabetical-book-types/', views.AlphabeticalBookTypesList.as_view()),
    path('books/search/', views.book_search),
    path('authors/search/', views.author_search),
    path('book-types/search/', views.book_type_search),
    path('books/<slug:book_type_slug>/<slug:author_slug>/<slug:book_slug>/', views.BookDetail.as_view()),
    path('books/<slug:author_slug>/', views.AuthorDetail.as_view()),
    path('books/<slug:book_type_slug>/', views.BookTypeDetail.as_view()),
]