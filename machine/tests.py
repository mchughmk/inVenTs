# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Machine

# Create your tests here.
class MachineTests(TestCase):
    def setUp(self):
        self.machine = Machine()
        
    def test_when_no_money_operate_returns_false(self):
        self.assertFalse(self.machine.has_money())
        
    def test_when_has_money_operate_returns_true(self):
        self.machine.money_inserted = 25
        self.assertTrue(self.machine.has_money())
        
    def test_current_balance(self):
        self.machine.money_inserted = 25
        self.assertEqual(0.25, self.machine.current_balance)