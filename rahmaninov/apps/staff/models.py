# -*- coding: utf-8 -*-
from django.db import models
from rahmaninov.apps.school.models import Department, Subject

class Role(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    department = models.ForeignKey(Department, null=True, blank=True, verbose_name='Тип')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Honour(models.Model):
    title = models.CharField(max_length=70, verbose_name='Титул')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Заслуга"
        verbose_name_plural = "Заслуги"


class Teacher(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Первая'),
        (2, 'Вторая'),
        (3, 'Высшая'),
    )
    last_name = models.CharField(max_length=50, verbose_name='Фмилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    picture = models.ImageField(max_length=10, upload_to='img/staff/', null=True, blank=True, verbose_name='Фото')
    honour = models.ForeignKey(Honour, null=True, blank=True, verbose_name='Заслуги')
    role = models.ForeignKey(Role, null=True, blank=True, verbose_name='Роль')
    category = models.SmallIntegerField(null=True, blank=True, choices=CATEGORY_CHOICES, verbose_name='Категория')
    subjects = models.ManyToManyField(Subject, null=True, blank=True, verbose_name='Предметы', through='TeacherSubject')
    from_year = models.SmallIntegerField(null=True, blank=True, verbose_name='Работает с')

    class Meta:
        unique_together = ("first_name", "last_name")
        verbose_name_plural = "Учителя"
        verbose_name = "Учитель"
        ordering = ["last_name"]

    def has_subjects(self):
        return self.subjects.exists()

    @property
    def is_olympiad_teaher(self):
        olympiad = Department.objects.get(id=2)
        departments = []
        for subject in self.subjects.all():
            departments.append(subject.department)
        if olympiad in set(departments):
            return True
        return False

    def __unicode__(self):
        return u'{0} {1} {2}'.format(
            self.last_name,
            self.first_name,
            self.patronymic
        )


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher)
    subject = models.ForeignKey(Subject)

    class Meta:
        ordering = ["subject"]

    def __unicode__(self):
        return u'{0} ({1})'.format(self.subject, self.teacher.last_name)
