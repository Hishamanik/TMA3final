from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from part4.api.api import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect('./login')

    return render(request, 'part4/index.html')

def computers(request):
    if not request.user.is_authenticated:
        return redirect('./login')

    computer_info = []
    computers = get_computers()
    for computer in computers:
        components = get_components_for_computer(computer['id'])
        computer_info.append({
            'components': components,
            'computer': computer
        })
    template = loader.get_template('part4/computers.html')
    context = {
        'computer_info': computer_info,
        'computers': computers
    }
    return HttpResponse(template.render(context, request))

def customize(request, id):
    if not request.user.is_authenticated:
        return redirect('../login')

    computer = get_computer(id)
    selected_components = get_components_for_computer(id)
    all_components = get_components()
    template = loader.get_template('part4/customize.html')
    context = { 
        'computer': computer,
        'selected_components': selected_components,
        'all_components': all_components
    }
    return HttpResponse(template.render(context, request))

def parts(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    return render(request, 'part4/parts.html')

def contact(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    return render(request, 'part4/contact.html')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('./login')

    user = request.user
    cart_info, total_price = get_user_cart(user)

    template = loader.get_template('part4/cart.html')
    context = {
        'cart_info': cart_info,
        'total_price': total_price
    }
    return HttpResponse(template.render(context, request))

def orders(request):
    if not request.user.is_authenticated:
        return redirect('./login')

    user = request.user
    orders, total_price = get_user_orders(user)
    print(orders)
    template = loader.get_template('part4/orders.html')
    context = {
        'order_info': orders,
        'total_price': total_price
    }

    return HttpResponse(template.render(context, request))

def create(request):
    return render(request, 'part4/create.html')

def login(request):
    return render(request, 'part4/login.html')