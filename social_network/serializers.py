from rest_framework import serializers
from .models import Friends,Requests
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class FriendsSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta:
        model = Friends
        fields = ('id', "source_user" ,"target_user" , "status" ,'created_at')

    def validate(self, data):
        source_user = data.get('source_user')
        target_user = data.get('target_user')
        status = data.get('status')

        if source_user == target_user:
            raise serializers.ValidationError("Source user and target user cannot be the same.")


        if Requests.objects.filter(source_user=source_user, target_user=target_user,status=status).exists():
            raise serializers.ValidationError("This combination of source user and target user already exists.")

        return data
    
class FriendsListSerializer(FriendsSerializer): 
    # name = serializers.char
    class Meta:
        model = Friends
        fields = ('id', "source_user" ,"target_user" , "status" ,'created_at')




class RequestsSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Requests
        fields = ('id', "source_user" ,"target_user" , "status", 'created_at')

    def validate(self, data):
        source_user = data.get('source_user')
        target_user = data.get('target_user')
        status = data.get('target_user')

        if source_user == target_user:
            raise serializers.ValidationError("Source user and target user cannot be the same.")


        if Requests.objects.filter(source_user=source_user, target_user=target_user,status=status).exists():
            raise serializers.ValidationError("This combination of source user and target user already exists.")

        return data
    
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     print("hereeeeeeee11create")
    #     return Requests.objects.create(**validated_data)

