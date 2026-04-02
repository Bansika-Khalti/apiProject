from rest_framework import serializers
from .models import Blog  # Space added after the dot

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # Option A: List specific fields
        fields = ['id', 'title', 'content'] 
        
        # Option B: Or use this shortcut to include everything automatically
        # fields = '__all__'