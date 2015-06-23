import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from .api_client import ApiClient


logger = logging.getLogger(__name__)


def homepage(request):
    return render(request, 'core/homepage.html')


def browse(request, browse_type):
    logger.debug("browsing %s", browse_type)
    client = ApiClient()
    data = {'browse_type': browse_type,
            'terms': client.browse(browse_type)}

    if browse_type == 'enforcements':
        return render(request, 'core/landing_enforcement_reports.html', data)
    elif browse_type == 'events':
        return render(request, 'core/landing_adverse_events.html', data)
    else:
        return render(request, 'core/landing_drug_labels.html', data)


def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        query_string = request.GET.get('q')
        browse_type = request.GET.get('browse_type')
        client = ApiClient()
        data = client.search(query_string, api=browse_type)

        if browse_type == 'enforcements':
            return render(request, 'core/details_enforcement_reports.html', data)
        elif browse_type == 'events':
            return render(request, 'core/details_adverse_events.html', data)
        else:
            return render(request, 'core/details_drug_labels.html', data)

    return HttpResponseBadRequest()


def result(request):
    return render(request, 'core/result.html')


def search_detail(request):
    results = {}
    if request.method == 'GET' and 'q' in request.GET:
        q = request.GET.get('q').strip()
        filter_string = request.GET.get('filter_string').strip()
        browse_type = request.GET.get('browse_type').strip()
        client = ApiClient()
        results = client.get_age_sex(browse_type, q, filter_string)
    return HttpResponse(results, content_type='application/json')