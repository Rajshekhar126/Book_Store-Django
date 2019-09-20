from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('orders/',views.orders,name='orders'),
    path('cart/',views.cart,name='cart'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('addproducts/',views.addproducts,name='addproducts')
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
