import csv
import requests
import io

from django_cron import CronJobBase, Schedule
from django.conf import settings

from .models import PriceList
from .sheet_info import *

class UpdatePrice(CronJobBase):
    RUN_EVERY_MINS = 15
    RUN_AT_TIMES = ['00:00']
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
    code = 'store.crons.UpdatePrice'

    def _getTSV(self, url):
        req = requests.get(url)
        req.encoding = 'utf-8'
        return io.StringIO(req.text)
    
    def _writeDB(self, input, key):
        for row in csv.DictReader(input, delimiter='\t'):
            if row[KEY_ITEM] == '' or row[KEY_PRICE] == '':
                continue
            
            PriceList.objects.create(
                species = key,
                item = row[KEY_ITEM],
                price = int(row[KEY_PRICE])
            )

    def do(self):
        PriceList.objects.all().delete()
        
        for k in STORE_URLS.keys():
            self._writeDB(self._getTSV(STORE_URLS[k]), k)

        print('SUCCESS')
        return 'SUCCESS'