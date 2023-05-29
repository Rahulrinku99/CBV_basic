from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.

# function based view
def fbv_views(request):
    return HttpResponse('this is function view')

# class based view
class cbv(View):
    def get(self,request):
        return HttpResponse('This is Class based view')
    
# function based view for templates
def fbv_html(request):
    return render(request,'fbv_html.html')

# class based view for templates
class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    
#handling forms by using FBV

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method == 'POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')


    return render(request,'fbv_form.html',d)

# Handling forms by using CBV

class cbv_form(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)

    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')