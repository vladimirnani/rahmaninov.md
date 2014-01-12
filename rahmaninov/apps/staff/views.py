from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from .models import Teacher
import service

@cache_page(24 * 60 * 60)
def staff(request):
    object_list = service.get_staff_ordered()
    keys = object_list.keys()
    return render_to_response('staff.html', RequestContext(request, locals()))


@cache_page(24 * 60 * 60)
def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    is_teacher = teacher.subjects.exists()
    return render_to_response('staff-detail.html', RequestContext(request, locals()))

