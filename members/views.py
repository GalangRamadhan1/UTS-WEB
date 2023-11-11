from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render())


def user(request):
    template = loader.get_template("user.html")
    return HttpResponse(template.render())


def order(request):
    template = loader.get_template("order.html")
    return HttpResponse(template.render())
