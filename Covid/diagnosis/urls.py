from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingView,name='landing'),
    path('form/', views.Prediction_view, name='form'),
    path('demo/', views.DemoView, name='demo'),
    path('pract/', views.PractView, name='pract')
]
