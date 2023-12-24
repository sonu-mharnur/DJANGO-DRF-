from rest_framework import serializers
from.models import *
from django.contrib.auth.models import User

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # field = ['name','age']
        # exclude = ['id']
        

    # def validate(self, data):
    #     if data['age']< 18:
    #         raise serializers.ValidationError({'error':"age cannot be  less than 18"})
        
    #     if data['name']:
    #         for n in data['name']:
    #             if n.isdigit():
    #                 raise serializers.ValidationError({'error':"name cannot be numebric"})

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoty
        fields = '__all__'

class Bookserializer(serializers.ModelSerializer):
    category = CategotySerializer()  # Use CategotySerializer for the category field

    class Meta:
        model = Book
        fields = '__all__'

#### jwt token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user