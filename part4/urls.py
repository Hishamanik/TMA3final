from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('computers', views.computers, name='computers'),
    path('customize/<int:id>', views.customize, name='customize'),
    path('parts', views.parts, name='parts'),
    path('cart', views.cart, name='cart'),
    path('orders', views.orders, name='orders'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('create', views.create, name='create'),
    path('api/', include('part4.api.urls'))
]