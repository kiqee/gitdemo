#coding=utf-8
from django.http import HttpResponse


def index_view(rquest):
    return HttpResponse('hello git')