from rest_framework import serializers
from .models import Profile,Projects
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio','profile_photo','user')
        
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'project_title', 'site_link', 'project_description', 'project','user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'profile', 'posts']