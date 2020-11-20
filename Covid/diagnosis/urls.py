from django.urls import path
from . import views

app_name = 'diagnosis'

urlpatterns = [
    path('', views.LandingView,name='landing'),
    path('predict/',views.PredictionView,name='predict')
]
