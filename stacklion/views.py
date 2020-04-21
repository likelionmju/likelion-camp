from django.shortcuts import render

# Create your views here.
def QnA(request):
    return render(request, "QnA.html")