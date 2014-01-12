# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator


class GalleryCollection(models.Model):
    _validator = RegexValidator(regex='^.{30,60}$', message='Длина строки ''30 - 60', code='nomatch')

    name = models.CharField(max_length=50, verbose_name='Название')
    photoset_id = models.TextField(verbose_name='Cет id')
    cover_photo = models.TextField(verbose_name='Обложка')
    description = models.CharField(max_length=50, verbose_name='Описание', validators=[_validator])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
