from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detect/', views.detect_fire, name='detect_fire'),
    path('alerts/', views.view_alerts, name='view_alerts'),
]