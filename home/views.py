from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        ctx = {}
        return render(request,'home/index.html',ctx)

class ContactView(View):
    """displays contact page"""
    def get(self,request,*args,**kwargs):
        ctx = {}
        return render(request, 'home/contact.html',ctx)

class AboutView(View):
    """displays about us page"""
    def get(self,request,*args,**kwargs):
        ctx = {}
        return render(request, 'home/about.html',ctx)