import json
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from part4.api.api import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from part4.models import Cart, Order, StoreUser
from django.contrib.auth import authenticate, login, logout


def components(request):
    components = get_components()
    return JsonResponse(components, safe=False)


# AUTH
def login_user(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(redirect_to='../../')
    else:
        return HttpResponseForbidden('Unable to login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='../../login')


def create_new_user_db(params):
    user = User.objects.create_user(
        params['userName'],
        params['email'],
        params['password']
    )
    user.last_name = params['lastName']
    user.first_name = params['firstName']
    user.save()
    return user

def create_new_store_user(user):
    
    su = StoreUser.objects.create(user=user)
    Cart.objects.create(store_user=su)
    Order.objects.create(store_user=su)

@csrf_exempt
def create_user(request):
    str = request.body.decode('utf-8')
    user_params = json.loads(str)

    user = create_new_user_db(user_params)
    create_new_store_user(user)

    return HttpResponseRedirect(redirect_to='../../')

@csrf_exempt
def add_computer_cart(request):
    body = request.body.decode('utf-8')
    selected = json.loads(body)
    user = request.user

    computer = create_new_computer(selected)
    assign_computer_user_cart(user, computer)

    return HttpResponseRedirect(redirect_to='../../cart')

def remove_computer_cart(request):
    computer_id = request.GET.get('id', '')
    delete_computer_from_cart(computer_id)
    return HttpResponseRedirect(redirect_to='../../cart')


def create_order(request):
    user = request.user
    create_user_order(user)
    return HttpResponseRedirect(redirect_to='../../orders')

def cancel_order(request):
    computer_id = request.GET.get('id', '')
    delete_computer_from_order(computer_id)
    return HttpResponseRedirect(redirect_to='../../orders')