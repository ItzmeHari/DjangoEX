from django.shortcuts import render
from django.http import HttpResponse


def show(http_request):
    msg='hello world'

    return HttpResponse(msg)
