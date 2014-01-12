from django import template

register = template.Library()

@register.inclusion_tag('date.html')
def render_date(date):
	return {'date':date}
