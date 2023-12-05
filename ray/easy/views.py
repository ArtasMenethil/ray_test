from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
from rest_framework import permissions, generics

from .models import News
from .serializers import NewsSerializer


@extend_schema(
    tags=['News'],
    summary="Лист news"
)
class NewsAPIView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(
    tags=['News'],
    summary="New"
)
class NewsUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [permissions.IsAuthenticated]
