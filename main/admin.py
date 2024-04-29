from django.contrib import admin
from django.utils.html import format_html

from .models import Product,Basket,Customer

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
               'id','title','selling_price','discount_price',
                'description','category','product_img']
    list_editable = ['selling_price','discount_price']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['image']
    
    # show product image in a readOnly field
    def image(self,instance):
        if instance.product_img.name != '':
            return format_html(
                f'<img src="{instance.product_img.url}" class="thumbnail" />')
        return ''
        
    class Media:
        css = {
            'all':['main/css/admin.css']
         }



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name']



@admin.register(Basket)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity','created_at']
    autocomplete_fields = ['user','product']

