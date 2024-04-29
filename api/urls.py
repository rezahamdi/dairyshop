from django.urls import path
from rest_framework import routers

from api import views 



# Router object to register our urls 
router = routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename='products')
router.register('customers',views.CustomerViewSet, basename='customers')
router.register('basket',views.BasketViewSet, basename='basket')

# Add urls to the urlpatterns
urlpatterns =  router.urls