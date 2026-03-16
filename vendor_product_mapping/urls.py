from django.urls import path
from .views import (
    VendorProductMappingList,
    VendorProductMappingDetail
)

urlpatterns = [
    path("", VendorProductMappingList.as_view()),
    path("<int:pk>/", VendorProductMappingDetail.as_view()),
]