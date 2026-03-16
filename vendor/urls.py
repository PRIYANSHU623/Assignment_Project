from django.urls import path
from .views import (VendorList, VendorDetail)

urlpatterns = [
    path("", VendorList.as_view()),
    path("<int:pk>/", VendorDetail.as_view()),
]