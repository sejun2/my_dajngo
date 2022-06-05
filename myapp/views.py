import random

from django.http import HttpResponse


# Create your views here.

def index(request):
    randomValue: float = random.random()
    return HttpResponse('<h1>Random</h1>' + str(randomValue))
    # return HttpResponse('Index')


def create(request):
    return HttpResponse('Create')


def read(request, id):
    return HttpResponse('Create ' + id)
