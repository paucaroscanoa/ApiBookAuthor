from catalogo.models import Author, book
from django.shortcuts import redirect, render
from catalogo.forms import modelbookform
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

class Authorlist(ListView):
    model= Author

class BookCreate(CreateView):
    model = book
    fields = '__all__'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class BookUpdate(UpdateView):
    model= book
    fields = '__all__'

def update_book(request,pk):
    if request.method == 'POST':
        data = request.POST

        author = Author.objects.get(pk=data['author'])

        books = book.objects.get(pk=pk)
        books.title = data['title']
        books.author = author
        books.editorial = data['editorial']
        books.year = data['year']
        books.volumen = data['volumen']
        books.save()
        return redirect('/catalogo')
    else:
        books = book.objects.get(pk=pk)
        form =modelbookform(book.__dict__) #request.POST
        return render(request, 'catalog/new.html', {"form":form})

def new_book(request):
    if request.method == 'POST':
        data = request.POST

        books = book()
        books.title = data['title']
        books.author = data['author']
        books.editorial = data['editorial']
        books.year = data['year']
        books.volumen = data['volumen']
        books.save()
        return redirect('/catalogo')
    else:
        form =modelbookform() #request.POST
        return render(request, 'catalog/new.html', {"form":form})

def get_books_by_editorial(request,editorial):
    books = book.objects.filter(editorial=editorial)
    year = request.GET.get("year")
    if year != None:
        books = books.filter(year=year)
    return render(request,'catalog/index.html',{'books':books}) 
# Create your views here.
def catalogo_list(request):
    books = book.objects.all()
    return render(request,'catalog/index.html',{'books':books}) 
