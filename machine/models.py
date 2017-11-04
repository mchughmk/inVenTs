# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Machine(models.Model):
    money_inserted = models.PositiveIntegerField(default=0)

    def has_money(self):
        return self.money_inserted > 0
   
    @property
    def current_balance(self):
        return self.money_inserted / 100.0


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    machine = models.ForeignKey(Machine, related_name='products')
    
    def __unicode__(self):
        return self.name
    