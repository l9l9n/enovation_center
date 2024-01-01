from django.urls import path
from .views import (
    SupportingOrganizationListCreateView, SupportingOrganizationDetailView
)

urlpatterns = [
    path('supporting-organizations/', SupportingOrganizationListCreateView.as_view(), name='supporting-organization-list'),
    path('supporting-organizations/<int:pk>/', SupportingOrganizationDetailView.as_view(), name='supporting-organization-detail'),
]
