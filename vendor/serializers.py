from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is reqiuired")
        return value  
    
    def validate_code(self, value):
        if not value:
            raise serializers.ValidationError("Code is required")
        
        if Vendor.objects.filter(code=value).exists():
            raise serializers.ValidationError("Vendor with this code already exists.")
        
        return value
    
    
    