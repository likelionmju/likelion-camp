from django.shortcuts import render, get_object_or_404

# Create your views here.
from hw.models import Homework


def main(request):
    homeworks = Homework.objects.all
    return render(request, "hw_main.html", {'homeworks':homeworks})

def detail(request, id):
    homework = get_object_or_404(Homework, pk=id)
    return render(request, "hw_detail.html", {'homework':homework})