# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Machine, Product

def index(request, *args, **kwargs):
    machine, created = Machine.objects.get_or_create(id=1)
    
    message = ''
    if 'coin_entered' in request.POST:
        insert_coin(machine, request.POST.get('coin_entered', 0))
    elif 'item' in request.POST:
        item_name = request.POST.get('item', '')
        product_selected = Product.objects.get(name=item_name)
        
        if operate(machine, product_selected):
            message = '{0} dispensed'.format(request.POST.get('item'), '')
        else:
            message = 'Item costs {0} cents'.format(product_selected.price)
    
    return render(request, 'machine/vending_machine.html', {"machine": machine, "message": message})

# Helpers 
def insert_coin(machine, amount):    
    machine.money_inserted += int(amount)
    machine.save()
    
def operate(machine, product_selected):
    if machine.money_inserted >= product_selected.price:
        machine.money_inserted = 0
        machine.save()
        return True
    else:
        return False