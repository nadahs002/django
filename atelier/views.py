from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    template = loader.get_template('acceuil.html')
    context = {
        'nom':'haoues',
        'prenom':'nada',
        'age':20,
        'sexe':'f',
        'adresse':'kelibia',
        'classe':'dsi23',
        'notes':[0, 19 , 18 , 19, 19.5] 
        
    }
    return HttpResponse(template.render(context, request))

def consulter(request):
    template = loader.get_template('notes.html')
    context = {
        'nom':'haoues',
        'prenom':'nada',
        'sexe':'f',
        'notes':[] 
        
    }
    return HttpResponse(template.render(context, request))    
        
    
def retourner(request):
 return HttpResponseRedirect(reverse('index'))