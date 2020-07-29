from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from datetime import datetime 
from django.core.paginator import Paginator
from hw.models import Homework, Submission, SubmissionFiles


# Create your views here.

def main(request):
    homeworks = Homework.objects.all
    hw_list = Homework.objects.values('id')
    homework_id = []
    confirm = {}
    for h in hw_list:
        homework_id.append(h['id'])

    for i in homework_id:
        sub = get_or_none(Submission, homework_id=i)
        confirm[i]=sub

    return render(request, "hw_main.html", {'homeworks':homeworks, 'confirm':confirm})

def detail(request, id):
    homework = get_object_or_404(Homework, pk=id)
    check = get_or_none(Submission, homework_id=homework)
    if check == None:
        check = 0

    return render(request, "hw_detail.html", {'homework':homework, 'check':check})

def submit(request, id):
    if request.method == 'POST':
        submission = Submission()
        submission.student = request.user
        submission.homework_id = Homework.objects.get(id=id)
        submission.register_date = timezone.datetime.now()
        submission.register_content = request.POST['submission_content']
        submission.save()
        for s_file in request.FILES.getlist('submission_files'):
            SFile = SubmissionFiles()
            SFile.submission = submission
            SFile.file = s_file
            SFile.save()
        return redirect('/hw')

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

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None