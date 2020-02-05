from django.shortcuts import render
from prot.models import Prot


def login(request):
    prot = Prot.objects
    return render(request, "login/login.html",{'prot':prot})