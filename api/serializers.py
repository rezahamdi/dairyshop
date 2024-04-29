from django.template.defaultfilters import slugify
import django.template.defaultfilters
from rest_framework import serializers
from main.models import Product,Customer,Basket


class ProductSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'selling_price',
            'discount_price',
            'description',
            'category',
            'product_img'
            )
        
        
    
   
class CustomerSerializer(serializers.ModelSerializer):
    
    # We didn't have the user to create a customer objet 
    # We get it from the request in view 
    def create(self, validated_data):
        user = self.context.get('user')
        return Customer.objects.create(
                user=user , **validated_data)

    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'state',
            'city',
            'mobile',
            'postal_code'
        )



class BasketSeralizer(serializers.ModelSerializer):

    # We didn't have the user to create a customer objet 
    # We get it from the request in view 
    def create(self,validated_data):
        user = self.context.get('user')
        return Basket.objects.create(user=user,**validated_data)
    class Meta:
        model = Basket
        fields = (
            'pk',
            'created_at',
            'product',
            'quantity'
        )