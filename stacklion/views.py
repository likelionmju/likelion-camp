from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.utils import timezone

from stacklion.models import Question, Answer


def QnA(request):
    if request.method == 'POST':
        question = Question()
        question.question_content = request.POST['question']
        question.question_file = request.FILES.get('question_file', None)
        question.asker = request.user
        question.pub_date = timezone.datetime.now()
        question.save()
        return redirect('/stacklion/')
    else:
        questions = Question.objects
        return render(request, "QnA.html", {'questions': questions})

@csrf_exempt
def refresh(request):
    if request.method == 'POST' and request.POST['val']=='answer':
        answer = Answer()
        answer.answerer = request.user
        answer.answer_content = request.POST['answer']
        answer.question_id = Question.objects.get(id=request.POST['question_id'])
        answer.save()
        return redirect('/stacklion/')

    if request.method == 'POST' and request.POST['val'] == 'revise' and request.POST['submit']=='확인':
        id = request.POST['id']
        question = get_object_or_404(Question, pk=id)
        question.question_content = request.POST['revise']
        # 나중에 파일도 해줄 것
        question.save()

        questions = Question.objects
        top = request.POST['scrolltop']
        return redirect('/stacklion/')

# def revise(request):
#     if request.method == 'POST':
