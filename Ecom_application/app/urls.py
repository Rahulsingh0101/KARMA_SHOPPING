from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('laptop/<int:id>',views.laptop),
    path('category/',views.category),
    path('checkout/',views.checkout),
    path('cart/',views.cart),                  
    path('confirmation/',views.confirmation),
    path('contact/',views.contact),
    path('elements/',views.elements),
    path('login/',views.login),
    path("rig/",views.registration),
    path('registration/',views.userregistration),
    path('singleblog/',views.singleblog),
    path('tracking/',views.tracking),
    path('singleproductpage/<str:id>',views.singleproducts),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),
    path('Customer_registration/',views.Customer_registration,name='Customer_registration'),
    path('userregistration/',views.userregistration,name='reform'),
    path('userlogin/',views.userlogin,name='reform'),
    path('logout/',views.logout,name='reform'),
    path('show_cart/',views.show_cart,name='show_cart'),
    # path('userlogout/',views.userlogout,name='userlogout'),

    # path('laptop/<int:subcategory_id>/', laptop, name='show_subcategory'),
    # path('categories/', views.category_list, name='category_list'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

