from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
