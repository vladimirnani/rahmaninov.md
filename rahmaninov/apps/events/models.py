# -*- coding: utf-8 -*-
from datetime import date
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=70, verbose_name='Событие')
    datetime = models.DateTimeField(verbose_name='Время')
    details = models.CharField(max_length=70, null=True, blank=True, verbose_name='Детали')

    @property
    def is_past(self):
        if date.today() > self.datetime.date():
            return True
        return False

    class Meta:
        verbose_name_plural = "События"
        verbose_name = "Событие"
        ordering = ["datetime"]

    def __unicode__(self):
        return u'{0} {1}'.format(self.title, self.datetime)
