# Generated by Django 3.2.13 on 2022-04-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Длина')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('subject', models.CharField(max_length=100, verbose_name='Жанр')),
                ('actor', models.CharField(max_length=100, verbose_name='Актёр')),
                ('actress', models.CharField(max_length=100, verbose_name='Актриса')),
                ('director', models.CharField(max_length=100, verbose_name='Режиссёр')),
                ('popularity', models.IntegerField(blank=True, null=True, verbose_name='Популярность')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['-popularity'],
            },
        ),
    ]
