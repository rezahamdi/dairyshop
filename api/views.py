from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .permission import IsAdminOrReadOnly
from .pagination import ProductPagination
from api import serializers as api_serializer
from main import models as main_model


#  API Views

class ProductViewSet(ModelViewSet):
    queryset = main_model.Product.objects.all()
    serializer_class = api_serializer.ProductSeralizer
    pagination_class = ProductPagination
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}


class CustomerViewSet(ModelViewSet):
    serializer_class = api_serializer.CustomerSerializer
    permission_classes = [IsAuthenticated]

    # Override the query to fliter the objects
    def get_queryset(self):
        return main_model.Customer.objects.filter(
             user = self.request.user)

    # Send user to the serializer class
    def get_serializer_context(self):
        return {'user':self.request.user}



class BasketViewSet(ModelViewSet):
    serializer_class = api_serializer.BasketSeralizer
    permission_classes = [IsAuthenticated]
    
    # Override the query to fliter the objects
    def get_queryset(self):
        return main_model.Basket.objects.filter(
            user=self.request.user)
    
    # Send user to the serializer class
    def get_serializer_context(self):
        return {'user':self.request.user}

    