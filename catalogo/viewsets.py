from catalogo.serializers import BookSerializer
from rest_framework import viewsets
from catalogo.models import book

class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer

