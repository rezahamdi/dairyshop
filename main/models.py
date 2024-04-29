from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



# Dairy categories 
CATEGORY_CHOICES =(
    ('CR','Curd'),
    ('ML','Milk'),
    ('MS','Milkshake'),
    ('YO','Yogurt'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
    )

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    selling_price  = models.DecimalField(
                 max_digits=8,decimal_places=0)
    discount_price = models.DecimalField(
                 max_digits=8,decimal_places=0)
    description = models.TextField()
    category = models.CharField(
                max_length=2,choices=CATEGORY_CHOICES)
    product_img = models.ImageField(upload_to = 'product')

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"



class Customer(models.Model):
    user = models.ForeignKey(
            User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.PositiveIntegerField(default=0)
    postal_code = models.PositiveIntegerField()
     
    class Meta:
        verbose_name = "مشتریان"
        verbose_name_plural = "مشتریان"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Basket(models.Model):
    id = models.UUIDField( 
            primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
            User,on_delete=models.CASCADE)
    product = models.ForeignKey(
            Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    
    class Meta:
        verbose_name = "محصولات سبد خرید"
        verbose_name_plural = "محصولات سبد خرید"


