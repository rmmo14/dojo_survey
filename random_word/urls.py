from django.urls import path
from . import views

urlpatterns = [
    path('', views.rand),
    path('random_word', views.rand),
    path('random_word/reset', views.reset),
]