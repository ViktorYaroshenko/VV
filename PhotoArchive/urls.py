from django.urls import path
from .views import PhotoListView, PhotoDetailView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),  # Список фото
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),  # Детальный просмотр
]