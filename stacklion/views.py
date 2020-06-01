from django.shortcuts import render, redirect

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

def refresh(request):
    if request.method == 'POST':
        answer = Answer()
        answer.answerer = request.user
        answer.answer_content = request.POST['answer']
        answer.question_id = Question.objects.get(id=request.POST['question_id'])
        answer.save()
        return redirect('/stacklion/')
#
# def revise(request):
#     if request.method == 'POST':
