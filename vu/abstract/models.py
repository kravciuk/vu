# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import os
import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import FileField, ImageField
from django.contrib.auth import get_user_model

from logging import getLogger
log = getLogger(__name__)

User = get_user_model()


class UniqueFileField(FileField):
    def generate_filename(self, instance, filename):
        _name, ext = os.path.splitext(filename)
        name = f'{uuid.uuid4().hex}{ext}'
        return super().generate_filename(instance, name)


class UniqueImageField(ImageField):
    def generate_filename(self, instance, filename):
        _name, ext = os.path.splitext(filename)
        name = f'{uuid.uuid4().hex}{ext}'
        return super().generate_filename(instance, name)


class Base(models.Model):
    created_at = models.DateTimeField(_(u'Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'Updated at'), auto_now=True)
    class Meta:
        abstract = True


class BaseWithUser(Base):
    user = models.ForeignKey(User, validators=_(u'User'), blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
