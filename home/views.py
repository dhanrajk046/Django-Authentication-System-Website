from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Password for test user is Harry$$$***000
# Create your views here.
def home(request):
    # print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "home.html")


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials

        else:
            return render(request, "login.html")
        # No backend authenticated the credentials

        # Check if user has entered correct credentials
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    # return render(request, 'index.html')
    return redirect("login")
