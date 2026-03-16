from rest_framework import serializers

from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def validate(self, data):
        course = data.get("course")
        certification = data.get("certification")
        primary_mapping = data.get("primary_mapping", False)

        if CourseCertificationMapping.objects.filter(
            course=course, certification=certification
        ).exists():
            raise serializers.ValidationError(
                "This course and certification mapping already exists."
            )
        if primary_mapping:
            if CourseCertificationMapping.objects.filter(
                course=course, primary_mapping=True
            ).exists():
                raise serializers.ValidationError(
                    "This course already has a primary certification mapping."
                )
        return data