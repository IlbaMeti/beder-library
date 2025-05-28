from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm, BookSearchForm

def book_list(request):
    books = Book.objects.all()
    search_form = BookSearchForm(request.GET)
    
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search')
        category = search_form.cleaned_data.get('category')
        availability = search_form.cleaned_data.get('availability')
        
        if search_query:
            books = books.filter(
                Q(title__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(isbn__icontains=search_query)
            )
        
        if category:
            books = books.filter(category=category)
            
        if availability:
            books = books.filter(availability=availability)
    
    # Pagination
    paginator = Paginator(books, 12)  # Show 12 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_form': search_form,
        'total_books': books.count()
    }
    return render(request, 'library/book_list.html', context)

from bson import ObjectId

def book_detail(request, pk):
    try:
        obj_id = ObjectId(pk)  # konverto string në ObjectId
    except Exception:
        raise Http404("Invalid book id")
    
    book = get_object_or_404(Book, pk=obj_id)
    return render(request, 'library/book_detail.html', {'book': book})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Libri "{book.title}" u shtua me sukses!')
            return redirect('book_detail', pk=str(book.pk))
        else:
            messages.error(request, 'Ka ndodhur një gabim. Ju lutem kontrolloni të dhënat.')
    else:
        form = BookForm()
    
    return render(request, 'library/book_form.html', {
        'form': form,
        'title': 'Shto Libër të Ri'
    })

from bson import ObjectId
from django.http import Http404

def book_update(request, pk):
    try:
        obj_id = ObjectId(pk)
    except Exception:
        raise Http404("Invalid book id")
    
    book = get_object_or_404(Book, pk=obj_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Libri "{book.title}" u përditësua me sukses!')
            return redirect('book_detail', pk=str(book.pk))
        else:
            messages.error(request, 'Ka ndodhur një gabim. Ju lutem kontrolloni të dhënat.')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'library/book_form.html', {
        'form': form,
        'book': book,
        'title': f'Edito Librin: {book.title}'
    })


def book_delete(request, pk):
    try:
        obj_id = ObjectId(pk)
    except Exception:
        raise Http404("Invalid book id")
    
    book = get_object_or_404(Book, pk=obj_id)
    
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'Libri "{title}" u fshi me sukses!')
        return redirect('book_list')
    
    return render(request, 'library/book_confirm_delete.html', {'book': book})


def dashboard(request):
    total_books = Book.objects.count()
    available_books = Book.objects.filter(availability='available').count()
    borrowed_books = Book.objects.filter(availability='borrowed').count()
    categories = Book.objects.values_list('category', flat=True).distinct()
    
    recent_books = Book.objects.all()[:5]
    
    context = {
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'categories_count': len(categories),
        'recent_books': recent_books,
    }
    return render(request, 'library/dashboard.html', context)