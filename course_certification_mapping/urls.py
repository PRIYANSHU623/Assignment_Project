from django.urls import path
from .views import (
    CourseCertificationMappingList,
    CourseCertificationMappingDetail
)

urlpatterns = [
    path("", CourseCertificationMappingList.as_view()),
    path("<int:pk>/", CourseCertificationMappingDetail.as_view()),
]