from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ProductView
from .serializers import ProductViewSerializer

class ProductViewViewSet(viewsets.ModelViewSet):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    permission_classes = [IsAuthenticated]
