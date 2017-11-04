# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Machine

def index(request, *args, **kwargs):
    machine, created = Machine.objects.get_or_create(id=1)
    
    message = ''
    if 'coin_entered' in request.POST:
        insert_coin(machine, request.POST.get('coin_entered', 0))
    elif 'item' in request.POST:
        if operate(machine):
            message = '{0} dispensed'.format(request.POST.get('item'), '')
        else:
            message = 'Item costs 35 cents'
    
    return render(request, 'machine/vending_machine.html', {"machine": machine, "message": message})

# Helpers 
def insert_coin(machine, amount):    
    machine.money_inserted += int(amount)
    machine.save()
    
def operate(machine):
    if machine.money_inserted >= 35:
        machine.money_inserted = 0
        machine.save()
        return True
    else:
        return False