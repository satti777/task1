from rest_framework import generics
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.views.generic import TemplateView


class UserCreate(generics.CreateAPIView):
    """
        A view for creating user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Signup(TemplateView):
    """
        for rendering signup template
    """
    template_name = 'signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/api/dashboard/')
        return super().dispatch(request, *args, **kwargs)
