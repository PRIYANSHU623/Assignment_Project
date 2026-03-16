from django.contrib import admin
from .models import ProductCourseMapping
# Register your models here.

@admin.register(ProductCourseMapping)
class ProductCourseMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'course_id', 'created_at', 'updated_at')
    search_fields = ('product__name', 'course__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('id',)  
    