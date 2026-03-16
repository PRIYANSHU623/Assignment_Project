from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is reqiuired")
        return value  
    
    def validate_code(self, value):
        if not value:
            raise serializers.ValidationError("Code is required")
        
        if Course.objects.filter(code=value).exists():
            raise serializers.ValidationError("Course with this code already exists.")
        
        return value
    
    
    