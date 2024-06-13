from django.shortcuts import render

def catalogo(request):
    return render(request, 'catalogo.html') 

def inicio(request):
    return render(request, 'inicio.html')

def checkout(request):
    return render(request, 'checkout.html')

def item(request):
    return render(request, 'item.html')