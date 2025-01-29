from xmlrpc.client import boolean

from rest_framework import serializers
from .models import Post,Category
import datetime

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'



    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.create_date = datetime.now()
        instance.title= instance.title.upper
        instance.write_date = datetime.datetime.now()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.write_date = datetime.datetime.now()
        instance.edited= True
        return instance
