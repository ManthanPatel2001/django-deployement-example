from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import webpage,Topic,AccessRecord
# Create your views here.


def hello(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    myDicts = {'insert_me':"Hello This is My render variable"}
    return render(request,'index.html',context=date_dict)


