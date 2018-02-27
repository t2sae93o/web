from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
   title = models.CharField(max_length=255)
   text = models.TextField()
   added_at = models.DateTimeField(auto_now=True)
   rating = models.IntegerField(default=0)
   author = models.ForeignKey(User, related_name='question_author', on_delete=models.DO_NOTHING(None, None, None, None))
   likes = models.ManyToManyField(User, related_name='question_likes')


class Answer(models.Model):
   objects = QuestionManager() 
   text = models.TextField()
   added_at = models.DateTimeField(auto_now=True)
   question = models.ForeignKey(Question, on_delete=models.DO_NOTHING(None, None, None, None))
   author = models.ForeignKey(User, related_name='answer_author', on_delete=models.DO_NOTHING(None, None, None, None))

