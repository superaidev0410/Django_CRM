from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from person.serializers import PersonalInfoSerializer
from person.models import PersonalInfo

# Create your views here.
@api_view(['POST'])
def add_items(request):
    item = PersonalInfoSerializer(data=request.data)
  
    # validating for already existing data
    if PersonalInfo.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
