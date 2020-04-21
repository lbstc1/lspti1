from datetime import date
from django.db import models

class StuReg(models.Model):
    sDoa=models.DateField(blank=True,null=True,default=date.today)
    sTime=models.CharField(max_length=10)
    sDob=models.DateField()
    sPhoto=models.ImageField(default="image")
    sSetno=models.IntegerField()
    sCourse=models.CharField(max_length=50)
    sBranch=models.CharField(max_length=50)
    sAttend=models.CharField(max_length=10)
    sName=models.CharField(max_length=50)
    sFather=models.CharField(max_length=50)
    sGender=models.CharField(max_length=10)
    sAddress=models.CharField(max_length=100)
    sPhone1=models.CharField(max_length=10)
    sPhone2 = models.CharField(max_length=10)
    sFee=models.IntegerField()
    sQualifaction=models.CharField(max_length=50)
    sComment=models.CharField(max_length=20)
    sExam=models.CharField(max_length=20)
    def __str__(self):
        return self.sName
