# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Homepage(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, "home.html")