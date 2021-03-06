from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.conf import settings
# Create your views here.

def homeworklist(request):
    posts = Post.objects
    return render(request, 'homeworklist.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request,'detail.html',{'post':post})

def new(request):
    if request.method == 'POST':
        post = Post()
        # post.author = request.user
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/homework/detail/'+str(post.id))
    else:
        return render(request,'new.html')

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
        post.save()
        return redirect('/homework/detail/'+str(post.id))
    else:
        # 수정 폼
        return render(request, 'edit.html', {'post': post})
