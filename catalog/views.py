from django.shortcuts import render

def con(request):

    return render(request, 'catalog/contacts.html')

def hom(request):
    return render(request, 'catalog/home.html')