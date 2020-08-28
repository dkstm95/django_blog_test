from django.contrib import admin
from django.urls import include, path

from health_tok_board import views

app_name = 'health_tok_board'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('<int:blog_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create', views.create, name='create'),
    path('newblog', views.blogpost, name='newblog'),
    path('navermap', views.navermap, name='navermap'),
]
