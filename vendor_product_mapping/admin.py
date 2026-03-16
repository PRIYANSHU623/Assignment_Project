from django.contrib import admin
from .models import VendorProductMapping
# Register your models here.

@admin.register(VendorProductMapping)
class VendorProductMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_id', 'product_id', 'created_at', 'updated_at')
    search_fields = ('vendor__name', 'product__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('id',)