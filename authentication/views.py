from .forms import *
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


#creating login page
def registerPage(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]

        if password == confirmPassword:
            if User.objects.filter(firstname = firstname).exists():
                return messages(request, "FGi")
            if User.objects.filter(lastname = lastname).exists():
                return messages(request,"Adfasdfa")
            
            usr = User.objects.create_user(firstname=firstname, lastname=lastname, email=email, password = password)
            usr.save()
            return messages(request,"User create successful")
        else:
            return messages("none")

    return render(request, "authentication/register.html")