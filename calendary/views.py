from email import message
from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from datetime import date, timedelta
from django.contrib import messages

from .models import * 
from .forms import *


class CustomMessageMixin:
    
    @property
    def success_msg(self):
        return False
    
    def form_valid(self, form):
        messages.success(self.request, self.success_msg) # import
        return super().form_valid(form)

    # при обновлении или удалении мы запоминаем id объекта в адресной строке
    # дочерние классы должны иметь success_url = reverse_lazy() и не должны переопределять данную функцию
    def get_success_url(self):
        return f'{self.success_url}?id={self.object.id}'


class Home(ListView):
    model = Day
    template_name = 'calendary/index.html'
    context_object_name = 'days'

    def get_queryset(self):
        # return Day.objects.filter(title__gte=date.today()) # прошлые дни не отображаются, но остаются  в БД
        return Day.objects.filter(title__gte='2022-01-01') # прошлые дни отображаются


class AddLesson(CustomMessageMixin, CreateView):
    form_class = FormLesson
    template_name = 'calendary/add_lesson.html'
    success_url = reverse_lazy('home')
    success_msg = 'Запись создана'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form.fields['date'].queryset = Day.objects.filter(title__gte=date.today()) # прошлые дни не попадут в выборку
        # form.fields['date'].queryset = Day.objects.filter(title__gte='2022-01-01') # в пет-проекте отображаются все дни
        return form
    

class LessonView(CustomMessageMixin, UpdateView):    
    model = Lesson
    template_name = 'calendary/lesson.html'
    form_class = FormLesson
    success_msg = 'Запись успешно обновлена'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['dates'] = Day.objects.filter(title__gte=date.today()) # прошлые дни не попадут в выборку
        context['dates'] = Day.objects.filter(title__gte='2022-01-01') # в пет-проекте отображаются все дни
        return context


class DeleteLesson(DeleteView):
    model = Lesson
    template_name = 'calendary/index.html'
    success_url = reverse_lazy('home')
    success_msg = 'Запись успешно удалена'

    # класс для вызова сообщения CustomMessageMixin не будет работать, потому что удаление происходит при помощи метода post
    # нужно изменить метод post
    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request, *args, **kwargs)

# def delete_lesson(request, pk, *args, **kwargs):
#     les_obj = Lesson.objects.get(pk=pk)
#     les_obj.delete()
#     return redirect('home')

def add_day_lesson(request, pk, *args, **kwargs):
    last_day = Day.objects.last().title
    last_day += timedelta(days=1)
    Day.objects.create(title=last_day)
    return redirect('lesson', pk)

def add_day(request, *args, **kwargs):
    last_day = Day.objects.last().title
    last_day += timedelta(days=1)
    Day.objects.create(title=last_day)
    return redirect('add_lesson')


