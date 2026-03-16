from django.urls import path
from .views import (
    ProductCourseMappingList,
    ProductCourseMappingDetail,
)

urlpatterns = [
    path("", ProductCourseMappingList.as_view()),
    path("<int:pk>/", ProductCourseMappingDetail.as_view()),
]