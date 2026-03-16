from django.contrib import admin
from .models import CourseCertificationMapping
# Register your models here.

@admin.register(CourseCertificationMapping)
class CourseCertificationMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'certification_id', 'created_at', 'updated_at')
    search_fields = ('course__name', 'certification__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('id',)