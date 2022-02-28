from django.shortcuts import render
from AppTwo.models import user
from AppTwo.forms import userForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,"<em>My Secound App<em>")

def help(request):
    return render(request,'help.html')

def users(request):
    database_detail = user.objects.order_by('first_name')
    user_details = {'details':database_detail}
    return render(request,'user.html',context=user_details)

@csrf_exempt
def signup(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return help(request)
        else:
            print("ERROR Buddy")
    return render(request,'signup.html',context={'form':form})

