from django.urls import path
from .views import \
    index, image, filter_category, search, create_image, edit_image, delete_image

urlpatterns = [
    path('index/', index, name='index'),
    path('image/<int:id>', image, name='image'),
    path('filter/<str:category_display>', filter_category, name='filter'),
    path('search/', search, name='search'),
    path('create/', create_image, name='create'),
    path('edit/<int:id>', edit_image, name='edit'),
    path('delete/<int:id>', delete_image, name='delete'),
]
