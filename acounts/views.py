# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
	#return HttpResponse("Hola!")
	numbers = [1,2,3,4,5]
	name = "Johan Mendez"
	args = {"myName" : name, "numbers":numbers}
	return render(request, "acounts/home.html",args)

