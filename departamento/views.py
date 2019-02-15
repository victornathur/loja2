from django.shortcuts import render
from django.http import HttpResponse
from . models import Camisa
from . forms import CamisaForm

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

def camisa_form(request):
    if (request.method == 'POST'):
        form = CamisaForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('/departamento/camisa/')
        else:
          return render(request, 'camisa/form.html', {'form':form})   
    else:
        form = CamisaForm()
        return render(request, 'camisa/form.html', {'form':form})

