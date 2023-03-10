from django.shortcuts import render,redirect
from . models import *
from app.models import *
from django.contrib import messages
from django.views import View

from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.


def adminlogin(request):
    return render(request, 'app/login.html')

def profile(request):
    c = Adminuser.objects.all()
    return render(request, 'app/profile.html', {'c':c})   

def upprofile(request):
    return render (request, 'app/upprofile.html')     

def showregistration(request):
    ab = Adminuser.objects.all()
    return render(request, 'app/registrations.html', {'ab':ab}) 

def adminindex(request):
    bc = Customer.objects.all()
    dc = Customer.objects.all().count()
    ec = Addproduct.objects.all().count()



    return render(request, 'app/index.html',{'bc':bc, 'dc':dc, 'ec':ec}) 

def adminproducts(request):
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    AC = Addproduct.objects.all()
    return render(request, 'app/products.html', {'category':category,
                                                   'subcat':subcat,
                                                   'AC':AC}) 

def adminprofile(request):
    ab = Customer.objects.all()
    dc = Customer.objects.all().count()
    ec = Addproduct.objects.all().count()
    return render(request, 'app/myprofile.html',{'ab':ab,'dc':dc,'ec':ec})                

def adminorders(request):
    bc = Customer.objects.all()
    return render(request, 'app/orders.html',{'bc':bc})       

def adminenquiries(request):
    return render(request, 'app/enquiries.html')     

def update(request):
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    return render(request, 'app/update.html',{'category':category,
                                            'subcat':subcat,})           
    
def adminregistration(request):
    return render(request, 'app/adminregistration.html')  



def admin_registration(request):
    if request.method == 'POST':
        name = request.POST['username']
        Email = request.POST['email']
        phone = request.POST['phone']
        adress = request.POST['adress']
        image = request.FILES.get('image')
        password = make_password(request.POST['password'])
        if Adminuser.objects.filter(phone=phone).exists():
            messages.error(request, "phone number already exists")
            return redirect('adminregistration/')

        elif Adminuser.objects.filter(email=Email).exists():
            messages.error(request, "email is already exists")
            return redirect('adminregistration/')

        else:
            Adminuser.objects.create(name=name, email=Email,
                                phone=phone, adress=adress,
                                 image=image, password=password,
                                )
            return redirect('/adminlogin/')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if Adminuser.objects.filter(email=email).exists():
            obj = Adminuser.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect('/adminindex/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('email  is not registered')


def productadd(request):
    if request.method == 'POST':
        title = request.POST['title']   
        selling_price = request.POST['selling_price']   
        discounted_price = request.POST['discounted_price']   
        description = request.POST['description']   
        brand = request.POST['brand']   
        category = request.POST['category']   
        subcategory = request.POST['subcategory'] 
        product_image = request.FILES.get('product_image')
        cat = Category.objects.get(id=category)
        sub = SubCategory.objects.get(id=subcategory)
        # upload = request.FILES['product_image']
        # print(product_image)
        # fss = FileSystemStorage()
        # fss.save(upload.name,upload)   


        Addproduct.objects.create(title=title,
                                  selling_price=selling_price,
                                  discounted_price=discounted_price,
                                  description=description,
                                  brand=brand,
                                  category=cat,
                                  subcategory=sub,
                                  product_image=product_image)

        return redirect('/')     

def remove_product(request, id):
    Addproduct.objects.filter(id=id).delete()
    return redirect('/adminproducts/')  

def remove_register_user(request, id):
    Adminuser.objects.filter(id=id).delete()
    return redirect('/showregistration/')  


# def hjhgjhgjh(request):
#     if request.method =='POST':
#         uid = request.POST['uid'] 
#         first_name = request.POST['first_name'] 
#         last_name = request.POST['last_name'] 
#         company_name = request.POST['company'] 
#         Emai_name = request.POST['Email'] 
#         phone_number = request.POST['Phone'] 

#         Student.objects.filter(id=uid).update(first_name=first_name,last_name=last_name,
#                                               company_name=company_name,Email_name=Emai_name,
#                                               phone_number=phone_number),

#         return redirect('/data')


def update_product(request,id):
    res = Addproduct.objects.get(id = id)
    return render(request,'app/update.html',context={'res':res})



def update_product_data(request):
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']   
        selling_price = request.POST['selling_price']   
        discounted_price = request.POST['discounted_price']   
        description = request.POST['description']   
        brand = request.POST['brand']   
        # category = request.POST['category']   
        # subcategory = request.POST['subcategory'] 
        # product_image = request.FILES.get('product_image')
        # cat = Category.objects.get(id=category)
        # sub = SubCategory.objects.get(id=subcategory)
        
        Addproduct.objects.filter(id=id).update(title=title,
                                            selling_price=selling_price,
                                            discounted_price=discounted_price,
                                            description=description,
                                            brand=brand,
                                          )

        return redirect('/')  

                                            

def update_registration(request,id):
    up = Adminuser.objects.get(id = id)
    return render(request,'app/upprofile.html',context={'up':up})
    #(request,'app/profile.html',context={'up':up})


def update_registration_data(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adress = request.POST.get('adress')

        Adminuser.objects.filter(id=id).update( name=name,
                                               email=email,
                                               phone=phone,
                                               adress=adress )

    return redirect('/')                                           
