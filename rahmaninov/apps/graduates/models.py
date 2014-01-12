# -*- coding: utf-8 -*-
from django.db import models


class Graduate(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, unique=True)
    year = models.SmallIntegerField(verbose_name='Год Выпуска')
    country = models.CharField(verbose_name='Страна', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"
        ordering = ["year", "name"]

    def __unicode__(self):
        return u'{0} {1}'.format(self.name, self.year)

