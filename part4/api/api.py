from part4.models import *


def buildComputerObj(spec):
    obj = {}
    obj['id'] = spec.computer.pk
    obj['name'] = spec.computer.name
    obj['price'] = spec.computer.price
    obj['components'] = {
        'cpu': spec.cpu.pk,
        'graphics': spec.graphics_card.pk,
        'hardDrive': spec.hard_drive.pk,
        'ram': spec.ram.pk,
        'os': spec.os.pk,
        'display': spec.display.pk,
        'soundCard': spec.sound_card.pk
    }
    return obj

def get_computers():
    specs = ComputerSpecs.objects.filter(computer__default=True)
    res = []
    for spec in specs:
        res.append(buildComputerObj(spec))
    return res

def get_computer(id):
    spec = ComputerSpecs.objects.filter(computer__id=id)[0]
    return buildComputerObj(spec)

def get_components():
    res = {
        'cpu': list(Cpu.objects.values()),
        'graphics': list(GraphicsCard.objects.values()),
        'hardDrive': list(HardDrive.objects.values()),
        'ram': list(Ram.objects.values()),
        'os': list(Os.objects.values()),
        'display': list(Display.objects.values()),
        'soundCard': list(SoundCard.objects.values()),
    }
    return res

def get_components_for_computer(id):
    computer = get_computer(id)
    all_components = get_components()
    components = {}
    for key in all_components.keys():
        for component in all_components[key]:
            if component['id'] == computer['components'][key]:
                components[key] = component
    return components

def get_component_details(components):
    all_components = get_components()
    component_details = {}
    for key in components.keys():
        for candidate in all_components[key]:
            if candidate['id'] == components[key]:
                component_details[key] = candidate
    
    return component_details

def create_new_computer(selected):
    computer_name = selected['name']
    computer_price = selected['price']
    components = selected['components']

    #1. Create the computer
    computer = Computer.objects.create(
        name=computer_name,
        price=computer_price,
    )

    #2. Create the spec
    cpu_id = components['cpu']
    graphics_id = components['graphics']
    hard_drive_id = components['hardDrive']
    ram_id = components['ram']
    os_id = components['os']
    display_id = components['display']
    sound_card_id = components['soundCard']

    ComputerSpecs.objects.create(
        computer=computer,
        cpu=Cpu.objects.filter(pk=cpu_id)[0],
        graphics_card=GraphicsCard.objects.filter(pk=graphics_id)[0],
        hard_drive=HardDrive.objects.filter(pk=hard_drive_id)[0],
        ram=Ram.objects.filter(pk=ram_id)[0],
        os=Os.objects.filter(pk=os_id)[0],
        display=Display.objects.filter(pk=display_id)[0],
        sound_card=SoundCard.objects.filter(pk=sound_card_id)[0],
    )

    return computer

def assign_computer_user_cart(user, computer):
    su = StoreUser.objects.filter(user__id=user.id)[0]
    cart = Cart.objects.filter(store_user__id=su.id)[0]
    computer.cart = cart
    computer.save()

    cart.total_price = round(cart.total_price + computer.price, 2)
    cart.save()

def delete_computer_from_cart(computer_id):
    to_delete = Computer.objects.filter(pk=computer_id)[0]
    cart = Cart.objects.filter(pk=to_delete.cart.id)[0]
    cart.total_price =  round(cart.total_price - to_delete.price, 2)

    if (cart.total_price <= 1):
        cart.total_price = 0


    cart.save()
    to_delete.delete()

def get_user_cart(user):
    su = StoreUser.objects.filter(user__id=user.id)[0]
    cart = Cart.objects.filter(store_user__id=su.id)[0]
    computers = Computer.objects.filter(cart__id=cart.id)
    formatted_cart = []
    for computer in computers:
        components = get_components_for_computer(computer.id)
        formatted_cart.append({
            'id': computer.id,
            'name': computer.name,
            'price': computer.price,
            'components': components
        })

    return formatted_cart, cart.total_price

def create_user_order(user):
    su = StoreUser.objects.filter(user__id=user.id)[0]
    computers = Computer.objects.filter(cart__store_user__id=su.id)
    cart = Cart.objects.filter(store_user__id=su.id)[0]
    order = Order.objects.filter(store_user__id=su.id)[0]
    for computer in computers:
        computer.cart = None
        computer.order = order
        computer.save()

    order.total_price += cart.total_price
    cart.total_price = 0
    order.save()
    cart.save()


def delete_computer_from_order(computer_id):
    to_delete = Computer.objects.filter(pk=computer_id)[0]
    order = Order.objects.filter(pk=to_delete.order.id)[0]
    order.total_price =  round(order.total_price - to_delete.price, 2)

    if (order.total_price <= 1):
        order.total_price = 0


    order.save()
    to_delete.delete()


def get_user_orders(user):
    su = StoreUser.objects.filter(user__id=user.id)[0]
    orders = Order.objects.filter(store_user__id=su.id)[0]
    computers = Computer.objects.filter(order__id=orders.id)
    formatted_orders = []
    for computer in computers:
        components = get_components_for_computer(computer.id)
        formatted_orders.append({
            'id': computer.id,
            'name': computer.name,
            'price': computer.price,
            'components': components
        })
    
    return formatted_orders, orders.total_price