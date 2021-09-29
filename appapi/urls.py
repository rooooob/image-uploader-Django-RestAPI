from django.urls import path
from . import views

app_name = 'appapi'

urlpatterns = [
    path('images/', views.images_view, name='images'),
    path('images/<int:pk>/', views.image_detail, name='image-detail'),
    path('images/create/', views.image_create, name='image-create'),
]