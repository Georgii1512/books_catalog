from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, UpdateView, DetailView
from .forms import CatalogBookForm, CatalogBookSearchForm
from .models import CatalogBook

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class CatalogBooksListView(ListView):
    template_name = 'books-list.html'
    queryset = CatalogBook.objects.all()
    context_object_name = 'catalog_books'


class CatalogBookCreateView(CreateView):
    template_name = 'catalog-book-create.html'
    form_class = CatalogBookForm
    success_url = reverse_lazy('catalog:books_list')
    context_object_name = 'catalog_book'

class CatalogBookDeleteView(DeleteView):
    template_name = 'catalog-book-delete.html'
    model = CatalogBook
    success_url = reverse_lazy('catalog:books_list')
    context_object_name = 'catalog_book'

    # Configured to use 'isbn' instead of 'pk'
    pk_url_kwarg = 'isbn'
    slug_field = 'isbn'
    slug_url_kwarg = 'isbn'

    def get_object(self, queryset=None):
        isbn = self.kwargs.get('isbn')
        book = CatalogBook.objects.get(isbn=isbn)
        return book


class CatalogBookUpdateView(UpdateView):
    template_name = 'catalog-book-update.html'
    model = CatalogBook
    form_class = CatalogBookForm
    context_object_name = 'catalog_book'
    success_url = reverse_lazy('catalog:books_list')

    # Configured to use 'isbn' instead of 'pk'
    pk_url_kwarg = 'isbn'
    slug_field = 'isbn'
    slug_url_kwarg = 'isbn'

    def get_object(self, queryset=None):
        isbn = self.kwargs.get('isbn')
        book = CatalogBook.objects.get(isbn=isbn)
        return book


class CatalogBookSearchView(DetailView):
    template_name = 'book-search.html'
    model = CatalogBook
    context_object_name = 'catalog_book'

    def get_object(self, queryset=None):
        isbn = self.request.GET.get('isbn')
        if isbn:
            book = CatalogBook.objects.get(isbn=isbn)
        else:
            book = None
        return book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['isbn'] = self.request.GET.get('isbn')
        context['search_form'] = CatalogBookSearchForm(self.request.GET)
        return context

    # D:\Marketplace\book_parcer\vivat_books_details.csv

