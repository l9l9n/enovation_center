from django.urls import path
from .views import InvestorListCreateView, InvestorDetailView


urlpatterns = [
    path('investors/', InvestorListCreateView.as_view(), name='investor-list'),
    path('investors/<int:pk>/', InvestorDetailView.as_view(), name='investor-detail'),
]
