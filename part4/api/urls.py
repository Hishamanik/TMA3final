from django.urls import path
from . import views

urlpatterns = [
    path('components', views.components, name='components'),
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/create', views.create_user, name='create'),
    path('cart/add', views.add_computer_cart, name='add_to_cart'),
    path('cart/remove', views.remove_computer_cart, name='delete_from_cart'),
    path('cart', views.get_user_cart, name='get_cart'),
    path('orders/create', views.create_order, name='create_order'),
    path('orders/cancel', views.cancel_order, name='cancel_order')
]