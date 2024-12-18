from django.shortcuts import render
from rest_framework import viewsets
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework.permissions import IsAdminUser

class AthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_files = ['title', 'genre', 'author']

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        genre = self.request.query_params.get('genre', None)
        author = self.request.query_params.get('author', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if genre:
            queryset = queryset.filter(genre__iexact=genre)
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        return queryset
    
