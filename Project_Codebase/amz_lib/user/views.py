from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import hashlib

# Create your views here.


def signupUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confpassword']
        username = hashlib.sha512(email.encode()).hexdigest()
        if(password == confirmPassword):
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.full_name = name
            user.save()

            messages.success(request, "Registered Successfully!")
            return redirect(request.META['HTTP_REFERER'])
            # return redirect("books")

    return redirect(request.META['HTTP_REFERER'])
    # return render(request, 'allbooks.html')


def loginUser(request):
    if request.method == 'POST':
        email = request.POST['loginEmailId']
        password = request.POST['loginPassword']
        email = email.lower()
        username = hashlib.sha512(email.encode()).hexdigest()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, "Logged In Successfully!")
            return redirect(request.META['HTTP_REFERER'])
            # return redirect("books")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect(request.META['HTTP_REFERER'])
            # return redirect("books")

    return redirect(request.META['HTTP_REFERER'])
    # return HttpResponse("404 - Not Found")


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect(request.META['HTTP_REFERER'])
    # return redirect("books")
