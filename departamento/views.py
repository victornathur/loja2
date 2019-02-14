from django.shortcuts import render
from django.http import HttpResponse
from . models import Camisa, Casual

def home(request):
    return render(request, 'home.html' ,{})

def camisa_list(request):
    camisas = Camisa.objects.all()
    return render(request, 'camisa/list.html', {'camisas':camisas})

def camisa_show(request, camisa_id):
    camisa = Camisa.objects.get(pk=camisa_id)
    return render(request, 'camisa/show.html', {'camisa':camisa})  

def casual_list(request):
    casuals = Casual.objects.all()
    return render(request, 'casual/list.html', {'casuals':casuals})

def casual_show(request, casual_id):
    casual = Casual.objects.get(pk=casual_id)
    return render(request, 'casual/show.html', {'casual':casual})  

# Create your views here.
