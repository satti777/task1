from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'Vehicle', VehicleViewSet)
router.register(r'Categories', CategoriesViewSet)
urlpatterns = [

    path('VehicleList/', VehicleList.as_view()),
    path('dashboard/', Dashboard.as_view()),

]

urlpatterns += router.urls
