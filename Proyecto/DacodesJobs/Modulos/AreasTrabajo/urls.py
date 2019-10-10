from django.urls import path
from .views import *

urlpatterns = [
    path('', Areas.as_view(), name = 'Areas'),
]
