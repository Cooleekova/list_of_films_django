from django.core.paginator import Paginator
from django.shortcuts import render

from films.models import Film

# Create your views here.


def film_list_view(request):
    """
    Return a queryset of all Film instances by default.
    Return filtered queryset if GET request contains filter queries.
    Pagination returns 8 entries per page.
    """
    qs = Film.objects.all()

    chosen_field = request.GET.get('select_field')
    chosen_option = request.GET.get('select_filter')
    search_query = request.GET.get('search_field')
    ordering = request.GET.get('ordering')

    if search_query != '' and search_query is not None:
        if chosen_option != '' and chosen_option is not None:
            if chosen_field == 'title':
                qs = Film.objects.filter_title(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'subject':
                qs = Film.objects.filter_subject(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'actor':
                qs = Film.objects.filter_actor(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'actress':
                qs = Film.objects.filter_actress(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'director':
                qs = Film.objects.filter_director(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'year':
                qs = Film.objects.filter_year(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'length':
                qs = Film.objects.filter_length(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'popularity':
                qs = Film.objects.filter_popularity(search_query=search_query, chosen_option=chosen_option)
        else:
            qs = None

    if ordering != '' and ordering is not None and ordering != 'Order by...':
        qs = qs.order_by(ordering)

    paginator = Paginator(qs, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    print(request.get_full_path)

    context = {
        'queryset': page.object_list,
        'ordering': ordering,
        'select_field': chosen_field,
        'select_filter': chosen_option,
        'search_field': search_query,
        'page': page,

    }
    return render(request, 'films_list.html', context)
