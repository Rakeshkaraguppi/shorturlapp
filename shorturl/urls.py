from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<short_url>/', views.redirect_to_url, name='redirect_to_url'),
]