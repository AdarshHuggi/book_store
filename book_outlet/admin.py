from django.contrib import admin

# Register your models here.
from .models import Book, Author,Address,Country

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",)}
    #displaying the columns in admin panel
    list_display =("title","author","rating",)

#registering the book and bookadmin models to display in admin panel
admin.site.register(Book,BookAdmin)

class AuthorAdmin(admin.ModelAdmin):

    #displaying the columns in admin panel
    list_display =("first_name","last_name","address",)
#registering the Author and AuthorAdmin to display in admin panel
admin.site.register(Author,AuthorAdmin)


class AddressAdmin(admin.ModelAdmin):
    #displaying the columns in admin panel
    list_display =("street","city","postal_code",)

admin.site.register(Address,AddressAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display =("name","code",)

admin.site.register(Country,CountryAdmin)
