from django.shortcuts import render, get_object_or_404
from hw.models import Homework, Submission, SubmissionFiles
from account.models import User


# Create your views here.
def main(request):
    homeworks = Homework.objects.all()
    percentage_list = []
    for homework in homeworks:
        submissions = Submission.objects.filter(homework_id=homework.id)
        complete_percentage = len(submissions) / len(User.objects.all()) * 100
        percentage_list.append(complete_percentage)

    return render(request=request, template_name='hw_manage_index.html', context={'homeworks': homeworks,
                                                                                  'percentage_list': percentage_list})


def detail(request, homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)
    users = User.objects.all()
    current_situations = []
    for user in users:
        submission_user = Submission.objects.get(student=user.pk, homework_id=homework.pk)
        if submission_user is None:
            response_data = {'name': user.name, 'is_submit': False}
        else:
            response_data = {
                'name': user.name,
                'is_submit': True,
                'register_date': submission_user.register_date,
                'register_content': submission_user.register_content,
                'has_file': False
            }
            file = SubmissionFiles.objects.filter(submission_id=submission_user.pk)
            if len(file) is not 0:
                response_data['has_file'] = True
                response_data['register_files'] = file
        current_situations.append(response_data)

    return render(request, template_name='hw_manage_detail.html', context={'title': homework.title,
                                                                           'current_situations': current_situations})
