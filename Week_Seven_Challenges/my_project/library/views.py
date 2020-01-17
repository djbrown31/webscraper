from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from library.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages']

def book_list(request, template_name='books/book_list.html'):
    books = Book.objects.all()
    data = {'all_books': books}
    return render(request, template_name, data)

def book_view(request, book_id, template_name='books/book_detail.html'):
    book = get_object_or_404(Book, id=book_id)
    data = {'book': book}
    return render(request, template_name, data)

def book_create(request, template_name='books/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form': form, 'new_or_edit': 'New'})

def book_update(request, book_id, template_name='books/book_form.html'):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form' :form, 'new_or_edit': 'Edit'})

def book_delete(request, book_id, template_name='books/book_confirm_delete.html'):
    book = get_object_or_404(Book, id=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object': book})
