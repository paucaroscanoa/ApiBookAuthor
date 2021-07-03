from catalogo.models import book, Author
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =['first_name','last_name','nationality','genere']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = book
        fields =['title','editorial','year','volumen','author']