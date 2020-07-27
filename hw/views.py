from django.shortcuts import render, get_object_or_404

# Create your views here.
from hw.models import Homework


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
        notice.register_date = request.POST['register_date']
        notice.author = request.user
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.end_date = request.POST['end_date']
        notice.notice_file = request.FILES.get('notice_file',None)
        notice.pub_date = timezone.datetime.now()
        notice.save()
        return redirect('/hw/hw_detail/'+str(notice.id))
    else:
        return render(request,'notice_new.html')