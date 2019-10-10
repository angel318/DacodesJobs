from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', Candidatos.as_view(), name = 'Candidatos'),
]
