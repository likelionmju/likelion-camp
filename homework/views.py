from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post,Notice
from django.conf import settings
# Create your views here.



def homeworklist(request):
    posts = Post.objects
    notices = Notice.objects
    return render(request, 'homeworklist.html', {'posts':posts,'notices':notices,'count':0})

def noticedetail(request, id):
    notice = get_object_or_404(Notice, pk=id)
    return render(request,'noticedetail.html',{'notice':notice})

def noticenew(request):
    if request.method == 'POST':
        notice = Notice()
        notice.author = request.user
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.notice_file = request.FILES.get('notice_file',None)
        notice.pub_date = timezone.datetime.now()
        notice.save()
        return redirect('/homework/noticedetail/'+str(notice.id))
    else:
        return render(request,'noticenew.html')

def noticedelete(request, id):
    notice = get_object_or_404(Notice, pk=id)
    notice.delete()
    return redirect('/homework/')

def noticeedit(request, id):
    notice = get_object_or_404(Notice, pk=id)
    
    if request.method == 'POST':
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.notice_file = request.FILES.get('notice_file',None)
        notice.save()

        return redirect('/homework/noticedetail/'+str(notice.id))
    else:
        
        return render(request, 'noticeedit.html', {'notice': notice})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request,'detail.html',{'post':post})

def homeworknew(request):
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.post_file = request.FILES.get('post_file',None)
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/homework/detail/'+str(post.id))
    else:
        return render(request,'homeworknew.html')

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('/homework/')

def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    # 수정 폼 제출
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.post_file = request.FILES.get('post_file',None)
        post.save()

        return redirect('/homework/detail/'+str(post.id))
    else:
        # 수정 폼
        return render(request, 'edit.html', {'post': post})



