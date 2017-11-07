from django.db import models
from django.utils import timezone

import datetime



class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        delta = timezone.now() - datetime.timedelta(days=1)
        return self.pub_date >= delta.date()


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        return self.choice_text



