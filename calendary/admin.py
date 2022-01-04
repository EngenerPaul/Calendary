from django.contrib import admin
from .models import *

from datetime import date, timedelta


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'pupil_name', 'pupils_father', 'theme', 'salary', 'time', 'date')
    list_display_links = ('id', 'pupil_name')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=None, change=False, **kwargs)
        form.base_fields['date'].queryset = Day.objects.filter(title__gte=date.today()) # прошлые дни не попадут в выборку
        return form

class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Day, DayAdmin)
