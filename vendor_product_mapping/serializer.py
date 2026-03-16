from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def validate(self, data):
        vendor = data.get("vendor")
        product = data.get("product")
        primary_mapping = data.get("primary_mapping", False)

        if VendorProductMapping.objects.filter(
            vendor=vendor, product=product
        ).exists():
            raise serializers.ValidationError(
                "This vendor and product mapping already exists."
            )

        if primary_mapping:
            if VendorProductMapping.objects.filter(
                vendor=vendor, primary_mapping=True
            ).exists():
                raise serializers.ValidationError(
                    "This vendor already has a primary product mapping."
                )

        return data
    
        
        
