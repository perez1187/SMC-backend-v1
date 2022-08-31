# from rest_framework import serializers


from rest_framework import serializers, validators
from . models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            "password": {"write_only":True},
            "id": {"read_only":True}
        }
    def create(self, validated_data):        
     
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = User.objects.create(

            password=password, 
            email=email,
            first_name=first_name,
            last_name=last_name 
        )
        return user