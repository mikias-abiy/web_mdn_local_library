from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre



def index(request):
    num_books = Book.objects.count()

    num_instances = BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }


    return render(request, 'catalog/index.html', context=context)
