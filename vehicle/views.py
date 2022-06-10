from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Categories instances.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing VehicleData instances.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = VehicleData.objects.all()
    http_method_names = ['post', 'put', 'patch', 'delete', 'head']


class VehicleList(generics.ListAPIView):
    """
    A viewset for viewing and filter VehicleData instances.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleListSerializer
    queryset = VehicleData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name', 'color', 'model', 'registration_no']


class Dashboard(LoginRequiredMixin, TemplateView):
    """
        for rendering dashboard template
    """
    template_name = 'dashboard.html'
    login_url = 'auth/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categories.objects.all()
        return context
