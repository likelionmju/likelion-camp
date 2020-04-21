from django.db import models

# Create your models here.
from account.models import User


class Question(models.Model):
    #pk 자동생성
    question_title = models.TextField(max_length=50, null=False, blank=False)
    question_content = models.TextField(null=False, blank=False)
    pub_date = models.DateField('date published')
    asker = models.ForeignKey(User, on_delete=models.PROTECT)