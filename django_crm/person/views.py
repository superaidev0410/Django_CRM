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
    # validating for correct field name
    for key in request.data.keys():
        if not key in ('first_name', 'last_name', 'birth_date', 'address1', 'address2', 
                        'city', 'county', 'state', 'zipcode', 'email', 'phone'):
            raise serializers.ValidationError(f'{key} is invalid field.')

    item = PersonalInfoSerializer(data=request.data)

    # check field existence
    is_firstname = True if 'first_name' in request.data.keys() and request.data['first_name'] != None else False
    is_lastname = True if 'last_name' in request.data.keys() and request.data['last_name'] != None else False
    is_email = True if 'email' in request.data.keys() and request.data['email'] != None else False
    is_phone = True if 'phone' in request.data.keys() and request.data['phone'] != None else False

    # validating for existence of first name and last name, email and phone
    if (is_firstname == False or is_lastname == False) and is_email == False and is_phone == False:
        raise serializers.ValidationError('At least input first and last name or email address or phone number.')
  
    # validating for already existing data
    if PersonalInfo.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items():
    
    # checking for the parameters from the URL
    items = PersonalInfo.objects.all()
  
    # if there is something in items else raise error
    if items:
        data = PersonalInfoSerializer(items, many=True).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    item = PersonalInfo.objects.get(pk=pk)
    data = PersonalInfoSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
