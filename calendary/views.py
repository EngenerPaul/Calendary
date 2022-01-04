from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from datetime import date, timedelta

from .models import * 
from .forms import *


class Home(ListView):
    model = Day
    template_name = 'calendary/index.html'
    context_object_name = 'days'

    def get_queryset(self):
        return Day.objects.filter(title__gte=date.today()) # прошлые дни не отображаются, но остаются  в БД


class AddLesson(CreateView):
    form_class = FormLesson
    template_name = 'calendary/add_lesson.html'
    success_url = reverse_lazy('home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].queryset = Day.objects.filter(title__gte=date.today()) # прошлые дни не попадут в выборку
        return form
    

class LessonView(DetailView, FormMixin):
    model = Lesson
    template_name = 'calendary/lesson.html'
    context_object_name = 'lesson'

    form_class = FormLesson

    # needed for updating page after save form
    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'slug':self.get_object().slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dates'] = Day.objects.filter(title__gte=date.today()) # прошлые дни не попадут в выборку
        return context


def delete_lesson(request, pk, *args, **kwargs):
    les_obj = Lesson.objects.get(pk=pk)
    les_obj.delete()
    return redirect('home')

def add_day_lesson(request, pk, *args, **kwargs):
    last_day = Day.objects.last().title
    last_day = last_day + timedelta(days=1)
    print(last_day)
    Day.objects.create(title=last_day)
    return redirect('lesson', pk)

def add_day(request, *args, **kwargs):
    last_day = Day.objects.last().title
    last_day = last_day + timedelta(days=1)
    Day.objects.create(title=last_day)
    return redirect('add_lesson')


