from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .models import PriceList, UpdateLog

import csv
import requests
import io
from datetime import datetime

KEY_ITEM = '品項'
KEY_PRICE = '單價'
URLs = {
    'snacks': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSDrekeIA76K7DtUQcIKMQeY4zSHyLHp4DSyVlHdfCbyYtJYl8C2ibOjUBEuuIY4c1K2z6auqVizMdn/pub?gid=460513074&single=true&output=tsv',
    'drink': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSDrekeIA76K7DtUQcIKMQeY4zSHyLHp4DSyVlHdfCbyYtJYl8C2ibOjUBEuuIY4c1K2z6auqVizMdn/pub?gid=1775519823&single=true&output=tsv',
    'noodles': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSDrekeIA76K7DtUQcIKMQeY4zSHyLHp4DSyVlHdfCbyYtJYl8C2ibOjUBEuuIY4c1K2z6auqVizMdn/pub?gid=1525551920&single=true&output=tsv',
    'other': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSDrekeIA76K7DtUQcIKMQeY4zSHyLHp4DSyVlHdfCbyYtJYl8C2ibOjUBEuuIY4c1K2z6auqVizMdn/pub?gid=138586683&single=true&output=tsv'
}

# Create your views here.
def home(request):
    return render(request, 'store/home.html', {
        'snacks': PriceList.objects.filter(species='snacks').order_by('price'),
        'drink': PriceList.objects.filter(species='drink').order_by('price'),
        'noodles': PriceList.objects.filter(species='noodles').order_by('price'),
        'other': PriceList.objects.filter(species='other').order_by('price'),
        'log': UpdateLog.objects.latest('date').date.strftime('%Y-%m-%d %H:%M:%S') if UpdateLog.objects.count() > 0 else ''
    })

def update(request):
    # flag = 'flag{xxx}'
    if request.GET.get('flag', default='') != flag:
        return redirect('home')

    if updateDB():
        return HttpResponse('UPDATE SUCCESS ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') )
    else:
        raise HttpResponse('UPDATE FAIL ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Update Database
def updateDB():
    try:
        PriceList.objects.all().delete()
        UpdateLog.objects.all().delete()

        for key in URLs.keys():
            writeDB( getTSV(URLs[key]), key)
        
        UpdateLog.objects.create(status='SUCCESS')
        return True
    except:
        try:
            UpdateLog.objects.create(status='FAIL')
        except:
            pass
        return False

def getTSV(URL):
    req = requests.get(URL)
    req.encoding = 'utf-8'
    return io.StringIO(req.text)

def writeDB(input, key):
    try:
        for row in csv.DictReader(input, delimiter='\t'):
            PriceList.objects.create(
                species = key,
                item = row[KEY_ITEM],
                price = int(row[KEY_PRICE])
            )
    except:
        raise HttpResponse('UPDATE FAIL ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))