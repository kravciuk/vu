# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django import template
from decimal import Decimal
from vu.math import Math

from logging import getLogger
log = getLogger(__name__)

register = template.Library()


@register.filter()
def multiply(source, amount):
    try:
        return Math.round(Decimal(source)*Decimal(amount))
    except Exception as e:
        log.error(e, exc_info=True)


@register.filter()
def minus(x, y):
    return x-y
