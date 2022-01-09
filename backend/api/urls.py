from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from django.urls import include
from rest_framework.routers import DefaultRouter

# from .viewsets import ItemViewSet
from .views import DetailItemView, ItemView

urlpatterns = [
    path("items/<int:pk>/", DetailItemView.as_view()),
    path("items/", ItemView.as_view()),
]
