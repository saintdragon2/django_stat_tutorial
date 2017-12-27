from django.shortcuts import render
from .models import Organization
# Create your views here.


def index(request):
    orgs = Organization.objects.all()

    return render(
        request,
        'rnd_survey/index.html',
        {
            'orgs': orgs,
        }

    )


def detail(request, org_id):
    org = Organization.objects.get(id=org_id)
    return render(
        request,
        'rnd_survey/detail.html',
        {
            'org': org,
        }
    )