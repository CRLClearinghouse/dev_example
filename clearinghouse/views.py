from django.shortcuts import render
from .models import *


def index_view(response):
    num_people = Person.objects.all().count()
    num_courts = Court.objects.all().count()
    try:
        num_people_courts = PersonCourt.objects.all().count()
    except:
        num_people_courts = 0
    return render(
        response,
        'clearinghouse/index.html',
        {
            'num_people': num_people,
            'num_courts': num_courts,
            'num_people_courts': num_people_courts,
        },
    )
