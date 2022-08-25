from rest_framework import serializers
from models import PersonalInfo


class PersonalInfoSerializer(serializers.ModelSerializer):
    """
    Serializer of PersonalInfo model
    """
    class Meta:
        model = PersonalInfo
        fields = ('first name', 'last name', 'birth date', 'address1', 'address2', 
                  'city', 'county', 'state', 'zipcode', 'email', 'phone')
