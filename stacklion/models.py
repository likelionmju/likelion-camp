from django.db import models

# Create your models here.
from account.models import User


class Question(models.Model):
    #pk 자동생성
    question_content = models.TextField(null=False, blank=False)
    pub_date = models.DateField('date published')
    asker = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.id)+str(self.asker)

class Answer(models.Model):
    answer_content = models.TextField(null=False, blank=False)
    answerer = models.ForeignKey(User, on_delete=models.PROTECT)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')