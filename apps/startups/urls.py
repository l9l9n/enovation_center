from django.urls import path
from .views import StartUpCreateAPIView

urlpatterns = [
    path('create/', StartUpCreateAPIView.as_view(), name='create-startup'),
]
