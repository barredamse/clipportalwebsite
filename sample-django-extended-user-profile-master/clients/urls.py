from django.urls import path
from clients import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
