from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
        "patients/", views.PatientListCreate.as_view(), name="patient-list"
    ),  # patient list view
    path(
        "patients/<int:pk>/",
        views.PatientRetrieveUpdateDestroy.as_view(),
        name="patient-detail",
    ),  # patient detail view
    path("", views.api_root),  # root view
]

urlpatterns = format_suffix_patterns(urlpatterns)
