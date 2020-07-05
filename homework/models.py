from django.db import models
from django.conf import settings
from account.models import User

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT,default='')
    pub_date = models.DateTimeField('publish')
    post_file = models.FileField(upload_to='files/', null=True, blank=True)
    content = models.TextField()




    def __str__(self):
        return self.title

class Notice(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.PROTECT,default='')
    pub_date = models.DateTimeField('publish')
    submitdate = models.DateTimeField(null=True, blank=True)
    notice_file = models.FileField(upload_to='files/', null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title