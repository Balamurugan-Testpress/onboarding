from django.db import models
from django.utils import timezone
import datetime  # Ensure this is imported

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("Date published")
    is_answered = models.BooleanField("Is this question is answered", default=False)
    is_correct = models.BooleanField("Is this question is correct", default=False)

    def __str__(self):
        return self.question_text

        
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1)).date()
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text