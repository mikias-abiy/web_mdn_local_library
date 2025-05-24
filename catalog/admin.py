from django.contrib import admin
from .models import Book, Author, Genre, BookInstance


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 3

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back') 

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')            
        }),
        ('Availablity', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Genre)
