from django.urls import path
from .views import StartupListCreateView, StartupDetailView

urlpatterns = [
    path('startups/', StartupListCreateView.as_view(), name='startups-list'),
    path('startups/<int:pk>/', StartupDetailView.as_view(), name='startups-detail'),
]
