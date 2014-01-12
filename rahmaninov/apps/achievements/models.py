# -*- coding: utf-8 -*-
from django.db import models
from rahmaninov.apps.school.models import Subject
from rahmaninov.apps.staff.models import Teacher
from rahmaninov.apps.pupils.models import Pupil


class LocationManager(models.Manager):

    def with_laureates(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute('''
            SELECT
            t.city,
            t.country,
            t.latitude,
            t.longitude,
            t.pupils
            FROM(
            SELECT
              l.country as country,
              l.city as city,
              l.latitude as latitude,
              l.longitude as longitude,
              (select array(
                 select distinct on (p.last_name) format('%s %s', p.last_name, p.first_name)
                 from achievements_laureatecompetition lc
                 left join pupils_pupil p on p.id = lc.laureate_id
                 where lc.competition_id in
                      (select c.id
                      from achievements_competition c
                      where l.id = c.location_id )
                 )) as pupils
            FROM
              public.achievements_location l
            ) t
            WHERE array_length(t.pupils, 1) > 0
        ''')
        result_list = []
        for row in cursor.fetchall():
            loc = {
                'city': row[0],
                'country': row[1],
                'lat': row[2],
                'lng': row[3],
                'laureates': row[4]
            }
            result_list.append(loc)
        return result_list


class Location(models.Model):
    """
    GeoLocation of event.
    """
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город')
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    objects = LocationManager()

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __unicode__(self):
        return u'{0} {1}'.format(self.country, self.city)


class Competition(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    location = models.ForeignKey(Location, verbose_name='Место')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Конкурсы'
        verbose_name = 'Конкурс'
        ordering = ['name']


class Olympiad(models.Model):
    OLYMPIAD_TYPE_CHOICES = (
        (1, 'Районная'),
        (2, 'Городская'),
        (3, 'Республиканская'),
        (4, 'Лицейская'),
    )
    NON_MUSICAL_DEPARTMENT_ID = 2

    subject = models.ForeignKey(Subject, verbose_name='Предмет', limit_choices_to={'department': NON_MUSICAL_DEPARTMENT_ID})
    olympiad_type = models.SmallIntegerField(null=True, blank=True, verbose_name='Тип', choices=OLYMPIAD_TYPE_CHOICES)

    def __unicode__(self):
        return u'{0} олимпиада {1}'.format(
            self.get_olympiad_type_display(),
            self.subject
        )

    class Meta:
        verbose_name_plural = 'Олимпиады'
        verbose_name = 'Олимпиада'


class LaureateManager(models.Manager):

    def get_queryset(self):
        query = super(LaureateManager, self).get_queryset() \
                                    .order_by('pupil__subject') \
                                    .select_related() \
                                    .exclude(competitions=None) \
                                    .prefetch_related('laureatecompetition_set')

        return query


class Laureate(models.Model):
    email = models.EmailField(null=True, blank=True)
    pupil = models.OneToOneField(Pupil, verbose_name='Ученик', primary_key=True)
    picture = models.ImageField(verbose_name='Фото', upload_to='img/laureates/', null=True, blank=True)
    details = models.TextField(verbose_name='Детали', null=True, blank=True)
    olympiads = models.ManyToManyField(Olympiad, through='LaureateOlympiad', null=True, blank=True)
    competitions = models.ManyToManyField(Competition, through='LaureateCompetition', verbose_name='Конкурсы')
    is_beginner = True
    this_year_laureate = False
    objects = LaureateManager()

    @property
    def name(self):
        return u'{0} {1}'.format(self.pupil.last_name, self.pupil.first_name)

    class Meta:
        verbose_name_plural = 'Лауреаты'
        verbose_name = 'Лауреат'
        ordering = ['pupil__last_name']

    def __unicode__(self):
        return u'{0}'.format(self.pupil)


class LaureateCompetition(models.Model):
    POSITION_CHOICES = (
        (0, 'Поощрение'),
        (1, 'I место'),
        (2, 'II место'),
        (3, 'III место'),
        (4, 'IV место'),
        (5, 'V место'),
        (6, 'Дипломант'),
        (7, 'I место. Золотая Медаль'),
        (8, 'II место. Серебряная Медаль'),
        (9, 'Участник'),
        (10, 'Приз зрительских симпатий'),
        (11, 'Приз симпатий жюри'),
        (12, 'Диплом I категории'),
        (13, 'Специальный диплом за артистизм'),
    )

    laureate = models.ForeignKey(Laureate, verbose_name='Лауреат')
    competition = models.ForeignKey(Competition, verbose_name='Конкурс')
    year = models.SmallIntegerField(verbose_name='Год')
    details = models.CharField(verbose_name='Детали', null=True, blank=True, max_length=50)
    position = models.SmallIntegerField(verbose_name='Место', choices=POSITION_CHOICES)

    class Meta:
        verbose_name_plural = 'Участия в конкурсах'
        verbose_name = 'Участие в конкурсе'
        ordering = ['year']


class LaureateOlympiad(models.Model):
    POSITION_CHOICES = (
        (1, 'I место'),
        (2, 'II место'),
        (3, 'III место'),
        (4, 'Поощрение'),
        (5, 'Благодарность за участие'),
    )

    laureate = models.ForeignKey(Laureate, verbose_name='Лауреат')
    olympiad = models.ForeignKey(Olympiad, verbose_name='Олимпиада')
    teacher = models.ForeignKey(Teacher, verbose_name='Учитель')
    position = models.SmallIntegerField(verbose_name='Место', choices=POSITION_CHOICES)
    year = models.SmallIntegerField(verbose_name='Год')

    class Meta:
        verbose_name_plural = 'Участия в олимпиадах'
        verbose_name = 'Участие в олимпиаде'
