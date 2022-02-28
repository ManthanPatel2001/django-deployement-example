from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'fourApp/index.html')

def other(request):
    contac_dir = { 'text':"You are in the Other Page Bro",'number':100}
    return render(request,'fourApp/other.html',contac_dir)