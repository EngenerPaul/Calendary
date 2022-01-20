from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('lesson/<int:pk>/', LessonView.as_view(), name='lesson'),
    path('addlesson/', AddLesson.as_view(), name='add_lesson'),
    path('delete-lesson/<int:pk>/', DeleteLesson.as_view(), name='delete_lesson'),
    # path('delete-lesson/<int:pk>/', delete_lesson, name='delete_lesson'),
    path('add_day/<int:pk>/', add_day_lesson, name='add_day_in_lesson'),
    path('add_day/', add_day, name='add_new_day'),
]