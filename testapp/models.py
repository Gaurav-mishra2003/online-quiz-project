from django.db import models

# Create your models here.
class addquiz_model(models.Model):
    ques=models.CharField(max_length=200)
    A=models.CharField(max_length=200)
    B=models.CharField(max_length=200)
    C=models.CharField(max_length=200)
    D=models.CharField(max_length=200)
    Ans=models.CharField(max_length=200)
class answer_model(models.Model):
    Selected_ans=models.CharField(max_length=80)
    unique_value1=models.IntegerField(default=1)

