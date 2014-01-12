from django.contrib import admin
from .models import Teacher, TeacherSubject, Role, Honour


class HiddenModelAdmin(admin.ModelAdmin):

    def get_model_perms(self, *args, **kwargs):
        perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
        perms['list_hide'] = True
        return perms


class HonourAdmin(HiddenModelAdmin):
    pass


class RoleAdmin(HiddenModelAdmin):
    pass



class TeacherSubjectInline(admin.TabularInline):
    model = TeacherSubject
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'patronymic',
        'category',
        'from_year'
    )
    list_display_links = ('last_name', 'first_name', 'patronymic')
    search_fields = ['last_name', 'first_name', 'patronymic']
    inlines = [TeacherSubjectInline]


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Honour, HonourAdmin)
admin.site.register(Role, RoleAdmin)

