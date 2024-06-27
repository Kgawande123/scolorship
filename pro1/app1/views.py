from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ScolorshipForm
from .models import Scolorship
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=("/a2/liv/"))
def sview(request):
    form = ScolorshipForm()
    if request.method == "POST":
        form = ScolorshipForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/a1/shv/")
    return render(request,"app1/scolorship.html",{"form":form})

def hview(request):
    return render(request,"app1/home.html",{})
@login_required(login_url=("/a2/liv/"))
def shview(request):
    obj = Scolorship.objects.all()
    return render(request,"app1/show.html",{"obj":obj})


def uview(request,pk):
    obj = Scolorship.objects.get(Id=pk)
    form = ScolorshipForm(instance=obj)
    if request.method == "POST":
        form = ScolorshipForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/shv/")
    return render(request,"app1/scolorship.html",{"form":form})


def dview(request,k):
    obj = Scolorship.objects.get(Id=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/shv/")
    return render(request,"app1/success.html",{"obj":obj})


