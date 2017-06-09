from rest_framework import serializers
from rentrightmodels.models import *
from datetime import datetime
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(email=validated_data['email'], first_name =validated_data['first_name'],last_name = validated_data['last_name'],username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
class identifier_serializer(serializers.ModelSerializer):
    user = CreateUserSerializer()  
    class Meta:
        model = identifier        
        fields = ('user','age', 'phone_number','address', 'profile_picture','first_name','last_name','username')
        extra_kwargs = {'activities': {'read_only': True}}
        def create(self, validated_data):
            who = '%s %s created a profile on %s' %( validated_data['first_name'], validated_data['last_name'], datetime.datetime.now)
            userlogs = user_logs (activity = who)
            userlogs.save()
            iden = identifier(**validated_data)
            iden.set_activities = userlogs
            iden.save()
            return userlogs                                                             
        def update(self, instance, validated_data):
            who = '%s %s updated his profile on %s' %( validated_data['first_name'], validated_data['last_name'],  datetime.datetime.now)             
            userlogs = user_logs (activity = who)
            userlogs.save()
            instance = identifier(**validated_data)
            instance.save();
            return userlogs
class locations_serializer(serializers.ModelSerializer):
    user = CreateUserSerializer()
    identifier = identifier_serializer()
    class Meta:
        model = locations
        fields = ('user', 'identifier', 'longitude', 'latitude', 'state', 'community', 'address')
class properties_log_serializer(serializers.ModelSerializer):
    user = CreateUserSerializer()
    identifier = identifier_serializer()
    class Meta:
        model = properties_log
        fields = ('user', 'identifier','cost', 'activity', 'comments' , 'event_date')    
    def create(self, validated_data):
        who = '%s %s registered a property on %s' %(validated_data.user.first_name, validated_data.user.last_name, datetime.datetime.now)
        prop = properties_log(**validated_data)
        prop.set_activity = who
        prop.save()
        return prop
class properties_serializer(serializers.ModelSerializer):
    manager = CreateUserSerializer()
    properties_log = properties_log_serializer()
    identifier = identifier_serializer()
    class Meta:
        model = properties
        fields = ('manager', 'identifier', 'status', 'availability', 'description', 'cost', 'community','address', 'properties_log' )

class occupants(serializers.ModelSerializer):
    user = CreateUserSerializer()
    properties = properties_serializer()
    identifier = identifier_serializer()
    class Meta:
        model = 
        fields = ('user', 'identifier', 'properties', 'status', 'tenancy_start', 'tenancy_end')

   
    
