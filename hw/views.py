from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator
from hw.models import Homework, Submission, SubmissionFiles


# Create your views here.

def hw_main(request):
    homeworks = Homework.objects.all
    hw_list = Homework.objects.values('id')
    homework_id = []
    confirm = {}
    for h in hw_list:
        homework_id.append(h['id'])

    for i in homework_id:
        sub = get_or_none(Submission, homework_id=i)
        confirm[i]=sub

    now = datetime.now()
    return render(request, "hw_main.html", {'homeworks':homeworks, 'confirm':confirm, 'now':now})

def detail(request, id):
    homework = get_object_or_404(Homework, pk=id)
    submission = get_or_none(Submission, homework_id=homework)
    if submission == None:
        submission = 0

    return render(request, "hw_detail.html", {'homework':homework, 'submission':submission})

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
        return redirect('/hw/detail/'+str(id))

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


def revise(request, id):
    if request.method == 'POST':
        if request.POST['submit'] == '확인':
            sub_id = request.POST['id']
            submission = get_object_or_404(Submission, pk=sub_id)
            submission.register_content = request.POST['revise']
            # 나중에 파일도 해줄 것
            submission.save()

            filelist = request.POST.getlist('filedelete')
            print(filelist)
            if filelist != None:
                for f in filelist:
                    file = get_object_or_404(SubmissionFiles, pk=f)
                    file.delete()
        if request.POST['submit'] == '삭제':
            sub_id = request.POST['id']
            submission = Submission.objects.get(pk=sub_id)
            submission.delete()
    return redirect('/hw/detail/' + str(id))



def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None