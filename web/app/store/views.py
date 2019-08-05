from django.views.generic import TemplateView
from django.conf import settings

from django_cron.models import CronJobLog
from .models import PriceList

class Home(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = PriceList.objects.filter(species='snacks').order_by('price')
        context['drink'] = PriceList.objects.filter(species='drink').order_by('price')
        context['noodles'] = PriceList.objects.filter(species='noodles').order_by('price')
        context['other'] = PriceList.objects.filter(species='other').order_by('price')
        context['log'] = None if not CronJobLog.objects.last() else CronJobLog.objects.last().end_time
        return context