from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from datetime import datetime
from elasticsearch import Elasticsearch
from base_app.forms import CityAddForm

# Create your views here.
class Index(TemplateView):
    """ Default Landing Page """
    template_name = 'base_app/base_app_index.html'


class HealthStatusView(TemplateView):
    """ All Incident Dashboard """
    template_name = 'base_app/base_app_health_status.html'

    def get_context_data(self, **kwargs):
        context = super(HealthStatusView, self).get_context_data(**kwargs)
        context['health_status'] = 'OK'
        return context


class CityListView(TemplateView):
    """ All city List """
    template_name = 'base_app/base_app_city_list.html'

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        es = Elasticsearch([settings.ELASTIC_ENDPOINT])
        result = es.search(index=settings.ELASTIC_INDEX_NAME, body={"query":{"match_all":{}}})
        city_dict = {}
        if result['hits']['hits']:
            for doc in result['hits']['hits']:
                city_dict[doc['_source']['city']] = doc['_source']['population']
        
        print(city_dict)
        context['city_dict'] = city_dict
        return context


class CityAddView(FormView):
    """ Add a new city """
    form_class = CityAddForm
    template_name = 'base_app/base_app_city_add_form.html'
    def get_success_url(self):
        return reverse_lazy('base_app:list-city')

    def form_valid(self, form):
        city = self.request.POST.get('city_name', False)
        population = self.request.POST.get('city_population', False)
        print(city)
        print(population)
        if False in [city, population]:
            print("Invalid input")
        else:
            es = Elasticsearch([settings.ELASTIC_ENDPOINT])
            doc = {
                'city': self.request.POST.get('city_name'),
                'population': self.request.POST.get('city_population'),
                'timestamp': datetime.now()
            }
            res = es.index(index=settings.ELASTIC_INDEX_NAME, id=city, document=doc)
            print(res)
        return super(CityAddView, self).form_valid(form)



