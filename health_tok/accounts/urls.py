from django.urls import path, include

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('social-login/', views.social_login, name='social_login'),
    path('social-accounts/', include('allauth.urls')),
]
