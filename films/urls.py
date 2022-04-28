from django.urls import path
from films.views import film_list_view

app_name = 'films'

urlpatterns = [
    path('', film_list_view, name='films-list-view'),
]
