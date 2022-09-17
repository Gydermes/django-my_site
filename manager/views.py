from django.shortcuts import HttpResponse


def add(request):
    return HttpResponse('manger add')


def delete(request):
    return HttpResponse('manger delete')


def edit(request):
    return HttpResponse('manger edit')
