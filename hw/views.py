from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from datetime import datetime 
from django.core.paginator import Paginator
from hw.models import Homework

# Create your views here.

def main(request):
    homeworks = Homework.objects.all
    latest_hw = Homework.objects.last()
    return render(request, "hw_main.html", {'homeworks':homeworks, 'lastest':latest_hw})

def detail(request, id):
    homework = get_object_or_404(Homework, pk=id)
    return render(request, "hw_detail.html", {'homework':homework})

def noticenew(request):
    if request.method == 'POST':
        notice = Homework()
        notice.register_date = timezone.datetime.now()
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.end_date = request.POST['end_date']
        notice.notice_file = request.FILES.get('notice_file',None)
        notice.save()
        return redirect('/hw')
        # detail 로 넘어가는거
    else:
        return render(request,'notice_new.html')