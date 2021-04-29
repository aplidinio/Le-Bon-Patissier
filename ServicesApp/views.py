from django.shortcuts import render
from ServicesApp.models import Service

# Create your views here.

def services(request):

    services = Service.objects.all()
    return render(request, "ServicesApp/services.html", {"services": services})