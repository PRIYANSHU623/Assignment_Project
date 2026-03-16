from django.db import models

# Create your models here.
class VendorProductMapping(models.Model):
    id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)