from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def siview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a2/liv/")
    return render(request,"authapp/sign.html",{"form":form})


def liview(request):
    if request.method == "POST":
        n = request.POST.get("unm")
        p = request.POST.get("pw")
        user = authenticate(username=n ,password=p)
        if user != None:
            login (request,user)
            return redirect("/a1/shv/")
    return render(request, "authapp/login.html", {})


def loview(request):
    logout(request)
    return redirect("/a2/siv/")
