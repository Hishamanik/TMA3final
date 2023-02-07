from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('computers', views.computers, name='computers'),
    path('customize/<int:id>', views.customize, name='customize'),
    path('parts', views.parts, name='parts'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('api/', include('part3.api.urls'))
]