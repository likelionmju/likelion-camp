from django.shortcuts import render

# Create your views here.

def homeworklist(request):
    return render(request, 'homeworklist.html')