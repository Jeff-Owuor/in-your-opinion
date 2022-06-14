from rest_framework import serializers
from .models import Profile,Projects




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio','profile_photo','user')
        
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'project_title', 'site_link', 'project_description', 'project','user']

