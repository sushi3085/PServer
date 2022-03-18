from django.urls import path
from . import views
 
urlpatterns = [
    path('callback', views.callback),
    path('getTry', views.getTry),
]