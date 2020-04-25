from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data


class IndexView(View):

    def get(self, request, *args, **kwargs):
        items = []

        city = None

        while not city:
            ret = get_client_data()
            if ret:
                city = ret[0]['city']
                ip_cliente = ret[1]

        q = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        location = city

        context = {
            'city': city,
            'busca': False,
            'ip_cliente': ip_cliente
        }

        if loc:
            location = loc
        if q:
            items = yelp_search(keyword=q, location=location)

            context = {
                'items': items,
                'city': location,
                'busca': True,
                'ip_cliente': ip_cliente
            }

        return render(request, 'index.html', context)