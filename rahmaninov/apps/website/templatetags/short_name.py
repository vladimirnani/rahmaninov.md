from django import template

register = template.Library()

@register.inclusion_tag('short_name.txt')
def short_name(teacher):
	name = u' {0} {1}. {2}.'.format(teacher.last_name, teacher.first_name[0], teacher.patronymic[0])
	return {'name':name}