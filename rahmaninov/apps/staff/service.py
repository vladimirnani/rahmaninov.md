from django.utils.datastructures import SortedDict
from rahmaninov.apps.school.models import Department
from .models import Teacher


def get_teachers(department):
    subjects = department.subject_set.all()
    teachers = list(Teacher.objects.filter(subjects__in=subjects).distinct())
    return teachers

def get_other_staff(department):
    staff = []
    for role in department.role_set.all():
        role_staff = role.teacher_set.order_by('last_name')
        staff += role_staff
    return staff

def get_staff_ordered():
    grouped_staff = SortedDict()

    for department in Department.objects.all():
        teachers = get_teachers(department)
        other_staff = get_other_staff(department)

        distinct = list(set(teachers + other_staff))
        staff = sorted(distinct, key=lambda x: x.id)
        grouped_staff[department.name] = staff

    return grouped_staff
