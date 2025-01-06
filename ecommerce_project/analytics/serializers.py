from rest_framework import serializers
from .models import ProductView

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = ['id', 'user', 'product', 'viewed_at']
