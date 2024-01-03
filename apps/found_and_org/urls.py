from django.urls import path
from .views import SupportingOrgCreateAPIView

urlpatterns = [
    path('create/', SupportingOrgCreateAPIView.as_view(), name='create-supporting-organization'),
]
