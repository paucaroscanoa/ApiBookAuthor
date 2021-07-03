from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=50)    
    genere = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.last_name},{self.first_name}"

class book(models.Model):
    title=models.CharField(max_length=45)
    #autor=models.CharField(max_length=45)
    year=models.IntegerField()
    editorial=models.CharField(max_length=25)
    volumen=models.IntegerField(null=True)
    price= models.FloatField(null=True)

    author= models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/catalogo"