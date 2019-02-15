from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Camisa, Casual
from . forms import CamisaForm, CasualForm

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

def casual_form(request):
    if (request.method == 'POST'):
        form = CasualForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('/departamento/casual/')
        else:
          return render(request, 'casual/form.html', {'form':form})   
    else:
        form = CasualForm()
        return render(request, 'casual/form.html', {'form':form})

def camisa_edit(request, camisa_id):
    if (request.method == 'POST'):
        camisa = Camisa.objects.get(pk=camisa_id)
        form = CamisaForm(request.POST, instance=camisa)
        if form.is_valid():
           form.save()
           return redirect('/departamento/camisa/')
        else:
           return render(request, 'camisa/edit.html', {'form':form,'camisa_id':camisa_id})
    else:
        camisa = Camisa.objects.get(pk=camisa_id)
        form = CamisaForm(instance=camisa)
        return render(request, 'camisa/edit.html', {'form':form,'camisa_id':camisa_id})
