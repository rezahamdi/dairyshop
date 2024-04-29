import json
import requests

from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.encoding import uri_to_iri
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Product,Basket
from .forms import CustomerRegistrationForm,LoginForm



# Template views Section

class HomeView(View):
    def get(self, request):
      context = {
                   'cart_count': cart_count(request)
                }
      return render(request,'main/home.html',context)




class CategoryView(View):
    def get(self, request, val):
        categories = Product.objects.filter(category=val)

        # Send date to the category template
        context = {
                'categories':categories,
                'cart_count': cart_count(request)
                  }
        return render(request,'main/category.html',context)


class SearchView(View):
    def get(self, request):
        query = request.GET.get('search',None)
        products = Product.objects.filter(
                 title__icontains = query)

        # Send date to the search template
        context = {
            'products' : products,
            'cart_count': cart_count(request),
        }
        return render(request,'main/search.html',context)



@method_decorator(login_required,name ='dispatch')
class MyProductDetailView(View):
    def get(self, request,slug):
        product = Product.objects.filter(slug = slug).first()
        
        # Send date to the detail template
        context ={
            'product': product,
            'cart_count': cart_count(request)
        }
        return render(request,'main/detail.html',context)






@method_decorator(login_required,name ='dispatch')
class BasketView(View):
    def get(self, request):
        cartItems = Basket.objects\
                 .select_related('product','user')\
                           .filter(user=request.user)
        
        # Send date to the basket template
        context = {
            'cartItems': cartItems,
            'cart_count': cartItems.count(),
            'total_cost': total_price(request)   
        }
        return render(request , 'main/basket.html',context=context)





#  =====  auth views Section

def customerRegister(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("home")
    else:
        form = CustomerRegistrationForm()

    # Send date to the register template
    context = {
          'form': form,
          'cart_count': cart_count(request),
        }
    return render(request,'main/register.html',context)

     
class UserLoginView(LoginView):
    template_name = 'main/login.html'
    authentication_form = LoginForm


def userlogout(request):
    logout(request)
    return redirect('login')





# ==== Js Views Section

def plusBasket(request):
    """
        Used to update our quantity in the basket
    """
    if request.method == 'GET':
        product_id = request.GET.get('prod_id')
        basket_item = Basket.objects\
                  .get(product=product_id,user=request.user)
        basket_item.quantity +=1
        basket_item.save()
        total = total_price(request)
        data ={
            "quantity":basket_item.quantity,
            "totalamount": f'{total:,}'
        }
        return JsonResponse(data)




def minusBasket(request):
    """
        Used to update our quantity in the basket
    """
    if request.method == 'GET':
        product_id = request.GET.get('prod_id')
        basket_item = Basket.objects\
                     .get(product=product_id,user=request.user)
        if basket_item.quantity > 1:
            basket_item.quantity -=1
            basket_item.save()

        total = total_price(request)

        # send data to update the front data
        data ={
            "quantity":basket_item.quantity,
            "totalamount": f'{total:,}'
        }
        return JsonResponse(data)



def deleteBasket(request):
    """
        Used to delete the product from our basket
    """
    if request.method == 'GET':
        product_id = request.GET.get('prod_id')
        basket_item = Basket.objects.filter(product=product_id).delete()
        basket =Basket.objects.filter(user=request.user)
        total = total_price(request)

        # send data to update the front data
        data ={
            "totalamount": f'{total:,}',
            "totalitem": basket.count()
        }
        return JsonResponse(data)



def addToBasket(request):
    """
        Used to create or update our basket 
    """
    if request.method == 'GET':
        product_id = request.GET.get('prod_id')

        #  With this try/except block if product exsists in the basket
        #  The quantity updated on the contrary our basket obj created 
        try:
            basket = Basket.objects\
                                 .get(
                                    product__id=product_id,
                                    user=request.user
                                    )
            basket.quantity +=1
            basket.save()
            
        except :
            product = Product.objects.get(id = product_id)
            basket = Basket.objects\
                        .create(
                            product=product,
                            user=request.user,
                            quantity = 1
                            )
    
    # send data to update the front data
    data ={
            "quantity": basket.quantity,
            "cart_count" : cart_count(request)
        }
    return JsonResponse(data)



# ==== DRY section 
def total_price(request):
    """
      This function used to calculate our basket total price
    """
    return sum([
        (basket.product.discount_price * basket.quantity)
                     for basket in\
                          Basket.objects\
                            .select_related('product','user')\
                                       .filter(user=request.user)
                ])

def cart_count(request):
    """
      This function used to count products in the our basket
    """
    basket_num = 0
    if request.user.is_authenticated:
        basket_num = Basket.objects\
                      .select_related('product','user')\
                          .filter(user=request.user).count()
    return basket_num

