# Generated by Django 4.0 on 2022-01-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['time'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='salary',
            field=models.IntegerField(default=700),
        ),
        migrations.AlterField(
            model_name='day',
            name='title',
            field=models.DateField(verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Было создано'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='note',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='pupil_name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='pupil_surname',
            field=models.CharField(blank=True, max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='pupils_father',
            field=models.CharField(blank=True, max_length=20, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.CharField(blank=True, max_length=30, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
    ]
