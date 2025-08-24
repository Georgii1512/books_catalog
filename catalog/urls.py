from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('catalog/book/<str:isbn>/update/', views.CatalogBookUpdateView.as_view(), name='book_update'),
    path('catalog/book/<str:isbn>/delete/', views.CatalogBookDeleteView.as_view(), name='book_delete'),
    path('', views.IndexView.as_view(), name='index'),
    path('catalog/create/', views.CatalogBookCreateView.as_view(), name='book_create'),
    path('catalog/books-list/', views.CatalogBooksListView.as_view(), name='books_list'),
    path('search/', views.CatalogBookSearchView.as_view(), name='book_search'),

]
