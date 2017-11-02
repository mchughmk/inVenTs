# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Machine(models.Model):
    money_inserted = models.PositiveIntegerField(default=0)

    def has_money(self):
        return self.money_inserted > 0