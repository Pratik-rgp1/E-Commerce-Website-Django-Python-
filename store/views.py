from django.shortcuts import render,  get_object_or_404
from .models import *
from django.http import JsonResponse
import json

def store(request):
    #valid customer with their total cart and wishlist items 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
        
    products = Product.objects.all()
    context = {'products' :products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def login(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()    
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
    
    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/login.html', context)

def home(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
        
    categories = Category.objects.all()
    context = {'categories' :categories, 'cartItems':cartItems}
    return render(request, 'store/home.html', context)

def category_product(request, category_id):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
    
    categories = Category.objects.all()
    try:
        category = get_object_or_404(Category, pk=category_id)
        catproducts = Product.objects.filter(category=category)
    # context = {'items':items, 'order': order, 'cartItems': cartItems, 'catproducts': catproducts},
    except Category.DoesNotExist:
        category = None
        catproducts = []
    
    context = {'items':items, 'order': order, 'cartItems': cartItems, 'catproducts': catproducts, 'category': category}
    return render(request, 'store/category_products.html', context)

# def category_travel(request, category_id):
    
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete= False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items=[]
#         order= {'get_cart_total' :0,'get_cart_items' :0,}
#         cartItems = order['get_cart_items']
    
#     categories = Category.objects.all()
#     try:
#         category = get_object_or_404(Category, pk=category_id)
#         catproducts = Product.objects.filter(category=category)
#     # context = {'items':items, 'order': order, 'cartItems': cartItems, 'catproducts': catproducts},
#     except Category.DoesNotExist:
#         category = None
#         catproducts = []
    
#     context = {'items':items, 'order': order, 'cartItems': cartItems, 'catproducts': catproducts, 'category': category}
#     return render(request, 'store/category_products.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()    
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
    
    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def booking(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, booking, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()    
        cartItems = order.get_cart_items
        bookings = booking.bookingtravel_set.all()
        bookTravels = booking.get_booking_travels
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        booking= {'get_booking_total' :0, 'get_booking_travels':0}
        cartItems = order['get_cart_items']
           
    context = {'items':items, 'order': order, 'cartItems': cartItems, 'bookings': bookings}
    return render(request, 'store/booking.html', context)

def view(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
        
    categories = Category.objects.all()
    context = {'categories' :categories, 'cartItems':cartItems}
    return render(request, 'store/view.html', context)


def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order= {'get_cart_total' :0,'get_cart_items' :0}
        cartItems = order['get_cart_items']
    
    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def main(request):
    context = {}
    return render(request, 'store/main.html', context)

def wishlist(request):
    context = {}
    return render(request, 'store/wishlist.html', context)

# def view(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete= False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items=[]
#         order= {'get_cart_total' :0,'get_cart_items' :0}
#         cartItems = order['get_cart_items']
    
#         categories = Category.objects.all()  
#         catproducts = Product.objects.filter(product.id=product)
#     # context = {'items':items, 'order': order, 'cartItems': cartItems, 'catproducts': catproducts},

#         catproducts = []
    
#     context = {'items':items, 'order': order, 'cartItems': cartItems, 'catproducts': catproducts, 'category': category}
#     return render(request, 'store/category_products.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete= False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was addded', safe=False)

# def updatebooking(request):
#     data = json.loads(request.body)
#     categoryTravelID = data['categoryTravelID']
#     action = data['action']
    
#     print('action:', action)
#     print('categoryTravelID:', categoryTravelID)
    
#     customer = request.user.customer
#     categoryTravel = categoryTravel.objects.get(id=categoryTravelID)
#     order, created = Order.objects.get_or_create(customer=customer, complete= False)
    
#     orderItem, created = OrderItem.objects.get_or_create(order=order, categoryTravel=categoryTravel)
    
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)
        
#     orderItem.save()
    
#     if orderItem.quantity <= 0:
#         orderItem.delete()
    
#     return JsonResponse('Item was addded', safe=False)

