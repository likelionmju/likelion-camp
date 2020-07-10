from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.utils import timezone

from stacklion.models import Question, QuestionFile, Answer


def QnA(request):
    if request.method == 'POST':
        if request.POST['submit']=='확인':
            id = request.POST['id']
            question = get_object_or_404(Question, pk=id)
            question.question_content = request.POST['revise']
            # 나중에 파일도 해줄 것
            question.save()
            # 코드 정리 좀 개더럽네 ㅁ;ㅣ아허
            questions = Question.objects
            top = request.POST['scrolltop']
            print(top)
            return render(request, "QnA.html", {'questions': questions, 'top':top})
        elif request.POST['submit']=='삭제':
            id = request.POST['id']
            question = get_object_or_404(Question, pk=id)
            question.delete()
            return redirect('/stacklion/')
    else:
        questions = Question.objects
        return render(request, "QnA.html", {'questions': questions})

def new(request):
    if request.method == 'POST':
        question = Question()
        question.question_content = request.POST['question']
        question.asker = request.user
        question.pub_date = timezone.datetime.now()
        question.save()

        for t_file in request.FILES.getlist('question_file'):
            QFile = QuestionFile()
            QFile.file = t_file
            QFile.question = question
            QFile.save()
        return redirect('/stacklion/')

@csrf_exempt
def refresh(request):
    if request.method == 'POST' and request.POST['val']=='answer':
        answer = Answer()
        answer.answerer = request.user
        answer.answer_content = request.POST['answer']
        answer.question_id = Question.objects.get(id=request.POST['question_id'])
        answer.save()
        return redirect('/stacklion/')



# def revise(request):
#     if request.method == 'POST':
