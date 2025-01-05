from django.views.generic import ListView, DetailView
from .models import Photo

# Отображение списка фотографий
class PhotoListView(ListView):
    model = Photo
    template_name = 'PhotoArchive/photo_list.html'  # Путь к шаблону
    context_object_name = 'photos'  # Имя переменной для контекста

# Детальное отображение одной фотографии
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'PhotoArchive/photo_detail.html'  # Путь к шаблону
    context_object_name = 'photo'  # Имя переменной для контекста
