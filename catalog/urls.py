from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalog/create/', views.CatalogBookCreateView.as_view(), name='book_create'),
    path('catalog/books-list/', views.CatalogBooksListView.as_view(), name='books_list'),
    path('catalog/book/<str:pk>/update/', views.CatalogBookUpdateView.as_view(), name='book_update'),
    path('catalog/book/<str:pk>/delete/', views.CatalogBookDeleteView.as_view(), name='book_delete'),

]