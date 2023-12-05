from django.urls import path
from rest_framework import routers
from .views import NewsAPIView, NewsUpdateAPIView

urlpatterns = [

    path('api/news/', NewsAPIView.as_view(), name='news'),
    path('api/new/<int:pk>', NewsUpdateAPIView.as_view(), name='new'),
]
