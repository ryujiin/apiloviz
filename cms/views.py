from django.shortcuts import render, render_to_response
from rest_framework import viewsets

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.

class TiendaView(TemplateView):
	template_name = "index.html"

# Create your views here.
