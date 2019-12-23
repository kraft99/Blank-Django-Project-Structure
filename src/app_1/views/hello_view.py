from django.shortcuts import render
from django.http import HttpResponse

from ..models import import_test

def hello_world(request):

	return HttpResponse("<h1>{0}</h1>".format(import_test()))