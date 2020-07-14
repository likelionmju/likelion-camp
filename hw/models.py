from django.db import models

# Create your models here.
from account.models import User


class Homework(models.Model):
    # 공지사항 등록/제목/공지내용/마감일/제출여부
    register_date = models.DateField('date published')
    title = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=False)
    end_date = models.DateField()
    # check 마감/진행중 나타내는 걸로 하자
    check = models.BooleanField(default=False)

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    homework_id = models.ForeignKey(Homework, on_delete=models.PROTECT, related_name="submission")
    register_date = models.DateField('date published')
    register_content = models.TextField(blank=True, null=True)

class SubmissionFiles(models.Model):
    file = models.FileField(upload_to="homework/")
    submission = models.ForeignKey(Submission, on_delete=models.PROTECT, related_name="files")

    def get_filename(self):
        fileName = str(self.file)[9:]
        return fileName
