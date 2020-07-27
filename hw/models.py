from django.db import models
from django.conf import settings
from account.models import User

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Homework(models.Model):
    # 공지사항 등록날짜/게시자/제목/공지내용/마감일/제출여부
    register_date = models.DateField('date published')
    author = models.ForeignKey(User, on_delete=models.PROTECT,default='')
    title = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=False)
    end_date = models.DateField()
    # check = 마감/진행중, confirm = 운영진 확인 여부
    check = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    homework_id = models.ForeignKey(Homework, on_delete=models.PROTECT, related_name="submission")
    register_date = models.DateField('date published')
    register_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class SubmissionFiles(models.Model):
    file = models.FileField(upload_to="homework/")
    submission = models.ForeignKey(Submission, on_delete=models.PROTECT, related_name="files")

    def get_filename(self):
        fileName = str(self.file)[9:]
        return fileName
