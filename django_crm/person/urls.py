from django.urls import path
from person.views import add_items, view_items

urlpatterns = [
   path('add/', add_items, name='add_items'),
   path('all/', view_items, name='view_items'),
]
