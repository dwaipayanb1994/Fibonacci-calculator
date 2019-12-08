from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cashback
from django.db.models import Sum
# Create your views here.

cb_rate = 0.1

def normalize(cashback):
    sm = Cashback.objects.aggregate(Sum('spends'))['spends__sum']
    for record in Cashback.objects.all():
        if record.spends:
            record.weight = sm / record.spends
        else:
            record.weight = 100000000000000000000000000000
        record.save()
    sm = Cashback.objects.aggregate(Sum('weight'))['weight__sum']
    for record in Cashback.objects.all():
        record.weight /= sm
        record.save()
    cb = Cashback.objects.aggregate(Sum('available_cashback'))['available_cashback__sum'] + cashback
    for record in Cashback.objects.all():
        record.available_cashback = cb * (0.2 + 0.4 * record.weight)
        record.save()

class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'cb1': Cashback.objects.values_list('available_cashback',
                flat=True)[0], 'cb2':Cashback.objects.values_list('available_cashback', flat=True)[1],
                'cb3':Cashback.objects.values_list('available_cashback', flat=True)[2]})

def form(request, pk):
    if request.method == 'POST':
        record = Cashback.objects.get(pk=pk)
        record.spends += int(request.POST['number'])
        record.save()
        normalize(int(request.POST['number']) * cb_rate)
    return HttpResponseRedirect(reverse('index'))
