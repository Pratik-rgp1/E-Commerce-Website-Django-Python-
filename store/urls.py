from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('cart/', views.cart, name="cart"),
    path('view/', views.view, name="view"),
    path('checkout/', views.checkout, name="checkout"),
    path('main/', views.main, name="main"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('booking/', views.booking, name="booking"),
    path('store/', views.store, name="store"),
    path('update_item/', views.updateItem, name="update_item"),
    # path('update_booking/', views.updatebooking, name="update_booking"),
    path('category_products/<int:category_id>/', views.category_product, name="category_products"),
]
