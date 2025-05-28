from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<str:pk>/', views.book_detail, name='book_detail'),  # ✅ ndryshuar nga <int:pk> në <str:pk>
    path('books/<str:pk>/edit/', views.book_update, name='book_update'),  # ✅ po ashtu
    path('books/<str:pk>/delete/', views.book_delete, name='book_delete'),  # ✅ po ashtu
]
