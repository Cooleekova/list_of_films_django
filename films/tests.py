from django.test import TestCase

# Create your tests here.

from .models import Film


class FilmTestCase(TestCase):
    """ TestCase for Film model"""

    def setUp(self):
        """ Create test instances of Film class """
        self.number_of_films = 10
        for i in range(0, self.number_of_films):
            Film.objects.create(
                year=2022,
                length=100,
                title='Film Title',
                subject='Film Subject',
                actor='Actor Name',
                actress='Actress Name',
                director='Director Name',
                popularity=50
            )

    def test_queryset_exists(self):
        """ Check if queryset was created """
        qs = Film.objects.all()
        self.assertTrue(qs.exists())

    def test_film_search_equals(self):
        """ Test filter option 'equals to' with each field of the model """
        qs = Film.objects.filter_year(search_query='2022', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_length(search_query='100', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_title(search_query='Film Title', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_subject(search_query='Film Subject', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_actor(search_query='Actor Name', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_actress(search_query='Actress Name', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_director(search_query='Director Name', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_popularity(search_query='50', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_films)

    def test_film_search_contains(self):
        """ Test filter option 'contains' with each field of the model """
        qs = Film.objects.filter_year(search_query='22', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_length(search_query='100', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_title(search_query='Film', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_subject(search_query='Subject', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_actor(search_query='Actor', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_actress(search_query='Actress', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_director(search_query='Director', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_popularity(search_query='50', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_films)

    def test_film_search_more_than(self):
        """ Test filter option 'more than' with integer fields of the model """
        qs = Film.objects.filter_year(search_query='2000', chosen_option='more than')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_length(search_query='200', chosen_option='more than')
        self.assertEqual(qs.count(), 0)
        qs = Film.objects.filter_popularity(search_query='40', chosen_option='more than')
        self.assertEqual(qs.count(), self.number_of_films)

    def test_film_search_less_than(self):
        """ Test filter option 'less than' with integer fields of the model """
        qs = Film.objects.filter_year(search_query='2023', chosen_option='less than')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_length(search_query='200', chosen_option='less than')
        self.assertEqual(qs.count(), self.number_of_films)
        qs = Film.objects.filter_popularity(search_query='40', chosen_option='less than')
        self.assertEqual(qs.count(), 0)
