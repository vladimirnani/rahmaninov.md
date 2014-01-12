# -*- coding: utf-8 -*-
from django.db import models
from rahmaninov.apps.school.models import Subject
from rahmaninov.apps.staff.models import Teacher


class Pupil(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    year_born = models.SmallIntegerField(verbose_name='Год рождения', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, verbose_name='Преподаватель Специальности')
    subject = models.ForeignKey(Subject, null=True, blank=True, verbose_name='Специальность')

    def __unicode__(self):
        return u'{0} {1}'.format(self.last_name, self.first_name)

    class Meta:
        verbose_name_plural = "Ученики"
        verbose_name = "Ученик"
        ordering = ["last_name", "teacher"]
        unique_together = ("first_name", "last_name")


class BaroccoMember(models.Model):
    pupil = models.OneToOneField(Pupil, verbose_name='Ученик', primary_key=True)
    instrument = models.ForeignKey(Subject, null=True, blank=True, verbose_name='Инструмент')

    class Meta:
        verbose_name = "Член Ансамбля"
        verbose_name_plural = "Состав Ансамбля Барокко"
        ordering = ["pupil__last_name"]

    def __unicode__(self):
        return unicode(self.pupil)

