from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True) #a user can have only one customer and a customer can have only one user
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
   
class Category(models.Model):
    # category_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # categoryProducts= models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    
    # des = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url
    
    #Travel and Adventure subcategory 
# class categoryProduct(models.Model):
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=200, null=True)
#     description = models.TextField(null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)
#     homestay = models.BooleanField(null=True, blank=True, default=False)
#     trekking_route = models.CharField(max_length=200, null=True, blank=True)
      
#     def __str__(self):
#         return self.name
    
#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#                 url= ''
#         return url
    
    
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transcation_id=models.CharField(max_length=200, null=True)
      
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping= True
        return shipping
        
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
        
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
  
class booking(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    booking_date=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transcation_id=models.CharField(max_length=200, null=True)
      
    def __str__(self):
        return str(self.id)  
    
    @property
    def get_booking_total(self):
        booktravels = self.booktravel_set.all()
        total = sum([booking.get_total for booking in booktravels])
        return total
        
    @property
    def get_booking_travels(self):
        bookingtravels = self.bookingtravel_set.all()
        total = sum([booking.quantity for booking in bookingtravels])
        return total
  
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    added_date=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
class ShippingAddress(models.Model): 
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    added_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.address)