
from django.urls import path
from . import views

app_name = 'WebPage1'
urlpatterns = [
    path('', views.index, name='index'),


]
