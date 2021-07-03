from catalogo.models import book, Author
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
class bookadmin(admin.ModelAdmin):
    list_display=('title','view_author','editorial','year','volumen','price_in_USD')

    def view_author(self, obj):
        if (obj.author != None):
            link = f"<a href='/admin/catalogo/author/{obj.author.id}/change/'>{obj.author}</a>"
            return format_html(link)
        else:
            return "-"

    def price_in_USD(self, obj):        
        if obj.price == None:
            f_price = 0.0
        else:
            f_price=float(obj.price)
        return f"$ {f_price}"
admin.site.register(book, bookadmin)

class authoradmin(admin.ModelAdmin):
    pass
admin.site.register(Author, authoradmin)