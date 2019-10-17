from django.urls import path
from imgsize import views

urlpatterns = [
    path('', views.get_imgsize),
]

