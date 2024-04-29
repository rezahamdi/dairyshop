from django.urls import path

from . import views 



urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('category/<str:val>/',views.CategoryView.as_view(), name = 'category'),
    path('basket/', views.BasketView.as_view(), name = 'basket'),
    path('search/',views.SearchView.as_view(), name = 'search'),
    path('detail/<slug:slug>', views.MyProductDetailView.as_view(), name = 'detail'),

    # Used for auth 
    path("logout", views.userlogout, name="logout"),
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
    path('registration/',views.customerRegister, name = 'customerregistration'),

    # Used for Js to update front data
    path('plusbasket/',views.plusBasket , name = 'plusbasket'),
    path('minusbasket/',views.minusBasket , name = 'minusbasket'),
    path('deletebasket/',views.deleteBasket , name = 'deletebasket'),
    path('addtobasket/',views.addToBasket , name = 'addtobasket'),
]
