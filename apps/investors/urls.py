from django.urls import path
from .views import InvestorCreateAPIView


urlpatterns = [
    path('create/', InvestorCreateAPIView.as_view(), name='create-investor'),
]
