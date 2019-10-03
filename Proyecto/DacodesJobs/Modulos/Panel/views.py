from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView

#Vistas
class PanelIndex(TemplateView):
    template_name = 'panel/index.html'
