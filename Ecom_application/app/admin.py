from django.contrib import admin

# Register your models here.
from app.models import *

@admin.register((User))
class UserModelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','password','is_active']                 



@admin.register((Addproduct))
class AddproductModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'selling_price', 'discounted_price'
                 ,'description','brand','category','subcategory','product_image']


@admin.register((Category))
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['id','name']                 

@admin.register((SubCategory))
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display=['id','name','category_id']                     


@admin.register((Cart))
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','product_id','category_id','Subcategory_id','title',
                     'brand','price','image',
                     'product_qty','total',
                     'user']     
    
          
@admin.register((Customer))
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','adress','city','state',
                    'zipcode','title','total' ,'ordered_date']            