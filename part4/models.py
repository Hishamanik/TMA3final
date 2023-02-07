from django.db import models
from django.contrib.auth.models import User

# Create your models here
class StoreUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Cart(models.Model):
    total_price = models.FloatField(default=0)
    store_user = models.ForeignKey(StoreUser, on_delete=models.CASCADE)

    def __str__(self):
        return 'Cart'


class Order(models.Model):
    total_price = models.FloatField(default=0)
    store_user = models.ForeignKey(StoreUser, on_delete=models.CASCADE)

    def __str__(self):
        return 'Order'


class Computer(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    default = models.BooleanField(default=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Cpu(Component):
    def __str__(self):
        return self.name

class GraphicsCard(Component):
    def __str__(self):
        return self.name

class HardDrive(Component):
    def __str__(self):
        return self.name

class Ram(Component):
    def __str__(self):
        return self.name

class Os(Component):
    def __str__(self):
        return self.name

class Display(Component):
    def __str__(self):
        return self.name

class SoundCard(Component):
    def __str__(self):
        return self.name


class ComputerSpecs(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE)
    hard_drive = models.ForeignKey(HardDrive, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    os = models.ForeignKey(Os, on_delete=models.CASCADE)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    sound_card = models.ForeignKey(SoundCard, on_delete=models.CASCADE)

    def __str__(self):
        return self.computer.name
