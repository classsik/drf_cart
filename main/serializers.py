from .models import Cart, Product
from rest_framework import serializers


class CartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
