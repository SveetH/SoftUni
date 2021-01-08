from django.urls import path

from pets.views import *

urlpatterns = [
    path('', list_pets, name='list pet'),
    path('details/<int:pk>/', show_pets_details, name='pet det'),
    path('like/<int:pk>/', like_pet, name='like pet'),
    path('edit/<int:pk>/', edit_pet, name='edit pet'),
    path('delete/<int:pk>/', delete_pet, name='delete pet'),
    path('create/', create_pet, name='create pet'),
]
