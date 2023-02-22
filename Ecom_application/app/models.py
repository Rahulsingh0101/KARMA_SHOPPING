from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100,blank=True,null=True)
    is_active=models.BooleanField(default=True)



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name


class Addproduct(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="productimg")

    def __str__(self):
        return str(self.id)





# class Cart(models.Model):
#     product = models.ForeignKey(Addproduct, on_delete=models.CASCADE)
#     product_qty = models.IntegerField()
#     total = models.IntegerField()
    

#     def __str__(self):
#         return str(self.id)

class Cart(models.Model):
    product_id = models.CharField(max_length=200)
    category_id= models.CharField(max_length=200)
    Subcategory_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image= models.CharField(max_length=200)
    product_qty = models.IntegerField()
    total = models.IntegerField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)



class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    adress=models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state=models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    ordered_date = models.DateTimeField(auto_now_add=True)
    # state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def __str__(self):
        return str(self.id)
 
    


