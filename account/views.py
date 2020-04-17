from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def logout(request):
        auth.logout(request)
        return redirect('home')

def register(request):
    return render(request, 'register.html')