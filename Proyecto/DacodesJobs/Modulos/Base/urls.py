from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', Index.as_view(), name = 'Index'),
    path('Nosotros', Nosotros.as_view(), name = 'Nosotros'),
    path('Staff/',login_required(StaffIndex.as_view()), name = 'StaffIndex'),
]
