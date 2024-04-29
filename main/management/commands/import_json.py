import os
import json

from django.core.management.base import BaseCommand
from  main.models import Product


class Command(BaseCommand):
    help = 'Populates the database with products'
    def handle(self, *args, **options):
        print('Populating the database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'data.json')
        with open(file_path,'r') as data:
            json_data = json.load(data)   
        for item in json_data:
            id = item.get('id')
            title = item.get('title')
            slug = item.get('slug')
            selling_price = item.get('selling_price')
            discount_price = item.get('discount_price')
            description = item.get('description')
            category = item.get('category')
            product_img = item.get('product_img')
            Product.objects.create(
                        id=id,title=title,slug = slug,category=category,
                        selling_price=selling_price, discount_price=discount_price,
                        description=description,product_img=product_img)
            

