from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import forms
# Create your views here.
@csrf_exempt
def basic(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation Success")
            print("name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("text: "+form.cleaned_data['text'])
    
    return render(request,'index.html',{'form':form})