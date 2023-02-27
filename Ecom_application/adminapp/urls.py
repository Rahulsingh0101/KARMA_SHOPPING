from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('adminlogin/',views.adminlogin),
   path('showregistration/',views.showregistration),
   path('adminindex/',views.adminindex),
   path('update/',views.update),
   path('adminproducts/',views.adminproducts),
   path('adminprofile/',views.adminprofile),
   path('adminorders/',views.adminorders),
   path('adminenquiries/',views.adminenquiries),
   path('adminregistration/',views.adminregistration),
   path('profile/',views.profile),
   path('upprofile/',views.upprofile),

   path('admin_registration/',views.admin_registration),
   path('admin_login/',views.admin_login),
   path('productadd/',views.productadd),
   path('update_product/<int:id>/',views.update_product),
   path('update_product_data/',views.update_product_data),
   path('update_registration_data/',views.update_registration_data),
   path('update_registration/<int:id>/',views.update_registration),
   path('remove_product/<int:id>',views.remove_product,name='remove_product'),
   path('remove_register_user/<int:id>',views.remove_register_user,name='remove_register_user'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

