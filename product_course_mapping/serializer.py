from rest_framework import serializers

from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def validate(self, data):
        product = data.get("product")
        course = data.get("course")
        primary_mapping = data.get("primary_mapping", False)

        if ProductCourseMapping.objects.filter(
            product=product, course=course
        ).exists():
            raise serializers.ValidationError(
                "This product and course mapping already exists."
            )
        if primary_mapping:
            if ProductCourseMapping.objects.filter(
                product=product, primary_mapping=True
            ).exists():
                raise serializers.ValidationError(
                    "This product already has a primary course mapping."
                )
        return data