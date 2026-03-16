from django.urls import path
from .views import CertificationList, CertificationDetail

urlpatterns = [
    path("", CertificationList.as_view()),
    path("<int:pk>/", CertificationDetail.as_view()),
]