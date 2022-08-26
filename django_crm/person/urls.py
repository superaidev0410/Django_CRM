from django.urls import path
from person.views import add_items

urlpatterns = [
   path('add/', add_items, name='add-items'),
]
