# -*- coding: utf-8 -*-
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='Отдел')
    order = models.SmallIntegerField(verbose_name='Порядок')
    is_musical = models.BooleanField(verbose_name='Музыкальный отдел')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        ordering = ["order"]


class Subject(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', unique=True)
    department = models.ForeignKey(Department, verbose_name='Отдел')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

