# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Machine

def index(request, *args, **kwargs):
    machine, created = Machine.objects.get_or_create(id=1)
    
    message = ''
    if 'insert_coin' in request.POST:
        insert_coin(machine)
        message = 'Balance: $0.25'
    elif 'operate' in request.POST:
        if operate(machine):
            message = 'Gumball dispensed'
        else:
            message = 'No money inserted'
    
    return render(request, 'machine/vending_machine.html', {"machine": machine, "message": message})

# Helpers 
def insert_coin(machine):    
    machine.money_inserted = 25
    machine.save()
    
def operate(machine):
    if machine.has_money():
        machine.money_inserted = 0
        machine.save()
        return True
    else:
        return False