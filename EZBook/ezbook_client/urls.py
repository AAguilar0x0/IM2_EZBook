from django.urls import path
from ezbook_client import views

app_name = 'ezbook_client'

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
]
