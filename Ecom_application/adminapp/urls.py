from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('adminlogin/',views.adminlogin),
   path('showregistration/',views.showregistration),
   path('adminindex/',views.adminindex),
   path('adminproducts/',views.adminproducts),
   path('adminprofile/',views.adminprofile),
   path('adminorders/',views.adminorders),
   path('adminenquiries/',views.adminenquiries),
   path('adminregistration/',views.adminregistration),

   path('admin_registration/',views.admin_registration),
   path('admin_login/',views.admin_login),
   path('productadd/',views.productadd),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

