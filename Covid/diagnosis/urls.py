from django.urls import path
from diagnosis import views

urlpatterns = [
    path('', views.LandingView.as_view(),name='landing'),
]
