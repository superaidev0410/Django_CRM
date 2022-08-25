from django.shortcuts import render
from rest_framework import viewsets
from person.serializers import PersonalInfoSerializer
from person.models import PersonalInfo

# Create your views here.
class PersonalInfoViewsets(viewsets.ModelViewSet):
    """
    Viewsets of PersonalInfo model
    """
    
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
