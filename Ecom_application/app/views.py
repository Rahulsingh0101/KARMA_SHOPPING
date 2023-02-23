from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.views import View
from . models import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.


def pro(request):
    return render(request, 'id/pro.html')


def proo(request):
    return render(request, 'id/proo.html')


def index(request):
    rahul = Addproduct.objects.all()
    # user = User.objects.filter(name=request.session["user_name"])
    return render(request, 'id/index.html', {'rahul': rahul, })


def cart(request):
    #     product = Addproduct.objects.all()
    #     carts=Cart.objects.all()
    return render(request, 'id/cart.html')
    # {"carts":carts,"product":product}


def laptop(request, id):
    ad = Addproduct.objects.filter(subcategory_id=id)

    return render(request, 'id/laptop.html', {'ad': ad})


def category(request):
    categories = Category.objects.all()
    product = Addproduct.objects.all()
    sub_c = SubCategory.objects.all()

    return render(request, 'id/category.html', {'categories': categories, 'product': product, 'sub_c': sub_c})


def checkout(request):
    carts = Cart.objects.all()
    product = Addproduct.objects.all()
    for c in carts:
        c.subtotal = float(c.product_qty) * float(c.price)
    
    subtotal = sum(c.subtotal for c in carts)
    total = float(subtotal)     
    return render(request, 'id/checkout.html', {"carts": carts,
                            "product": product,  'subtotal': subtotal,
                            'total': total, })


def confirmation(request):
    carts = Cart.objects.all()
    product = Addproduct.objects.all()
    cous = Customer.objects.all()
    print(cous)
    print("aaaaaaaaaaaaaaa")
    return render(request, 'id/confirmation.html', {"carts": carts,
                                                    "product": product,
                                                    "cous": cous})


def contact(request):
    return render(request, 'id/contact.html')


def elements(request):
    return render(request, 'id/elements.html')


def login(request):
    return render(request, 'id/login.html')


def registration(request):
    return render(request, 'id/registration.html')


def singleblog(request):
    return render(request, 'id/single-blog.html')


def tracking(request):
    return render(request, 'id/tracking.html')


def userregistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        Email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "phone number already exists")
            return redirect('registration/')

        elif User.objects.filter(email=Email).exists():
            messages.error(request, "email is already exists")
            return redirect('registration/')

        else:
            User.objects.create(name=name, email=Email,
                                phone=phone, password=password)
            return redirect('/login/')

    # create login form


def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            user_name = obj.name
            user_id = obj.id
            if check_password(user_password, password):
                request.session['name'] = user_name
                request.session['user_id'] = user_id
                print(request.session)
                return redirect('/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('email  is not registered')


def logout(request):
    request.session.clear()
    print(request.session)
    print("----------------------")
    return redirect('/login/')


def singleproducts(request, id):
    prod = Addproduct.objects.get(id=id)
    context = {
        'prod': prod
    }
    return render(request, 'id/single-product.html', context)


# def add_to_cart(request, id):
#     cart_items = Addproduct.objects.all()
#     Cart.objects.create(product_id=id, product_qty=1, total=0)

#     return redirect('/show_cart/')

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        category_id = request.POST['category_id']
        Subcategory_id = request.POST['Subcategory_id']
        product_qty = request.POST['product_qty']
        title = request.POST['title']
        brand = request.POST['brand']
        price = request.POST['price']
        image = request.POST['image']
        user_id= request.session['user_id']
        # user = User.objects.get(id=9)
        total = float(price) * float(product_qty)

        Cart.objects.create(product_id=product_id,
                            category_id=category_id,
                            Subcategory_id=Subcategory_id,
                            title=title, brand=brand, price=price,
                            image=image,product_qty=product_qty, 
                            total=total, user_id=user_id)

        return redirect('/show_cart/')


def show_cart(request):
    #cart = Cart.objects.get(product_id=id)
    cart_items = Cart.objects.all()
    product = Addproduct.objects.all()

    context = {
        'cart_items': cart_items,
        'product': product, }


    return render(request, 'id/cart.html', context)


def remove_cart(request, id):
    Cart.objects.filter(id=id).delete()
    return redirect('/show_cart/')


def Customer_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        Email = request.POST['email']
        adress = request.POST['adress']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        title = request.POST['title']
        total = request.POST['total']
        ordered_date = request.POST['ordered_date']
        prod=Cart.objects.all()
        titl = " "
        tit = 0
        for item in prod:
           titl += item.title
        for itm in prod:
           tit += itm.total

        context = {
        'prod': prod,  }

        Customer.objects.create(name=name, email=Email, phone=phone,
                                adress=adress, city=city, state=state,
                                 zipcode=zipcode,title=titl,total=tit,
                                 ordered_date=ordered_date)
        return redirect('/confirmation/')


