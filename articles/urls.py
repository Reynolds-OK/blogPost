from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('search/', views.search, name='search'),
    path('comments/<int:id>/', views.comments, name='comments'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('likes/<slug:slug>/', views.likes, name='likes'),
    path('<slug:slug>/<int:id>/', views.article_detail, name='detail'),
]
