from django.db import models

# Create your models here.


class CustomQuerySet(models.QuerySet):

    def filter_year(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(year__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(year__iexact=search_query)
        elif chosen_option == 'more than':
            return self.filter(year__gte=search_query)
        elif chosen_option == 'less than':
            return self.filter(year__lte=search_query)
        else:
            return self.none()

    def filter_length(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(length__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(length__iexact=search_query)
        elif chosen_option == 'more than':
            return self.filter(length__gte=search_query)
        elif chosen_option == 'less than':
            return self.filter(length__lte=search_query)
        else:
            return self.none()

    def filter_title(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(title__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(title__iexact=search_query)
        else:
            return self.all()

    def filter_subject(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(subject__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(subject__iexact=search_query)
        else:
            return self.all()

    def filter_actor(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(actor__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(actor__iexact=search_query)
        else:
            return self.all()

    def filter_actress(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(actress__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(actress__iexact=search_query)
        else:
            return self.all()

    def filter_director(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(director__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(director__iexact=search_query)
        else:
            return self.all()

    def filter_popularity(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(popularity__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(popularity__iexact=search_query)
        elif chosen_option == 'more than':
            return self.filter(popularity__gte=search_query)
        elif chosen_option == 'less than':
            return self.filter(popularity__lte=search_query)
        else:
            return self.none()


class Film(models.Model):

    year = models.IntegerField(
        verbose_name='Год',
    )

    length = models.IntegerField(
            blank=True,
            null=True,
            verbose_name='Длина',
        )

    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )

    subject = models.CharField(
        max_length=100,
        verbose_name='Жанр',
    )

    actor = models.CharField(
        max_length=100,
        verbose_name='Актёр',
    )

    actress = models.CharField(
        max_length=100,
        verbose_name='Актриса',
    )

    director = models.CharField(
        max_length=100,
        verbose_name='Режиссёр',
    )

    popularity = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Популярность',
    )

    objects = CustomQuerySet.as_manager()

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-popularity', ]

    def __str__(self):
        return self.title


