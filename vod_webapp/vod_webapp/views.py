from django.shortcuts import render
from django.template import Context


def landing(request):
    context = Context({})
    return render(request, "landing.html", context)