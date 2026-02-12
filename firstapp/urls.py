from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello),
    path('class', views.HelloEthiopia.as_view()),
]