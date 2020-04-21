from django import forms
from.models import *
from datetime import date

class StuRegForm(forms.ModelForm):
    sTime_cho = (('',''),('7:00 AM', '7:00 AM'), ('8:00 AM', '8:00 AM'),('9:00 AM', '9:00 AM'),('10:00 AM','10:00 AM'),('11:00 AM','11:00 AM'),
                 ('12:00 PM','12:00 PM'),('1:00 PM','1:00 PM'),('2:00 PM','2:00 PM'),('3:00 PM','3:00 PM'),('4:00 PM','4:00 PM'),
                 ('5:00 PM','5:00 PM'),('6:00 PM','6:00 PM'),('7:00 PM','7:00 PM'),)
    sAttend_cho = (('Yes', 'Yes'), ('No', 'No'),)
    sSetno_cho = (('',''),('1', '1'), ('2', '2'),)
    sCourse_cho = (('',''),('P-CCS','P-CCS'), ('P-CCH','P-CCS'), ('P-CFA','P-CFA'), ('P-DOM','P-DOM'), ('P-CDTP','P-CDTP'),
                   ('CES', 'CES'),('P-AFA', 'P-AFA'), ('P-ADCA', 'P-ADCA'), ('P-CCP', 'P-CCP'), ('C-DCA', 'C-DCA'),
                   ('P-CWD', 'P-CWD'),('P-DIT', 'P-DIT'),)
    sBranch_cho = (('',''),('Nangloi', 'Nangloi'), ('Vikas Nagar', 'Vikas Nagar'),)
    sGender_cho = (('',''),('Male', 'Male'), ('Female', 'Female'),)
    sExam_cho = (('Yes', 'Yes'), ('No', 'No'),)
    sComment_cho=(('ID_No','ID_No'),('Leave','Leave'),('No Information','No Information'),)
    sQuali_cho = (('',''),('< 8th Class','< 8th Class'),('9th Class','9th Class'),('10th Class','10th Class'),('12th Class','12th Class'),
                  ('Graduation','Graduation'),('P.G.','P.G.'),)
    sFee_cho=(('',''),('500','500'),('550','550'),('600','600'),('650','650'),('700','700'),('750','750'),('800','800'),('850','850'),('900','900'),
              ('950','950'),('1000','1000'),('1100','1100'),('1200','1200'),('1300','1300'),('1400','1400'),('1500','1500'),('1600','1600'),
              ('1800','1800'),('2000','2000'),('2500','2500'),('3000','3000'),('3500','3500'),('4000','4000'),('4500','4500'),('5000','5000'),('5500','5500'),('6000','6000'),)

    YEARS = [x for x in range(1980, 2012)]

    sSetno = forms.CharField(widget=forms.Select(choices=sSetno_cho, attrs={'class': 'form-control'}))
    sTime = forms.CharField(widget=forms.Select(choices=sTime_cho, attrs={'class': 'form-control'}))
    sAttend=forms.CharField(widget=forms.Select(choices=sAttend_cho,attrs={'class':'form-control'}))
    sCourse = forms.CharField(widget=forms.Select(choices=sCourse_cho, attrs={'class': 'form-control'}))
    sBranch = forms.CharField(widget=forms.Select(choices=sBranch_cho, attrs={'class': 'form-control'}))
    sGender = forms.CharField(widget=forms.Select(choices=sGender_cho, attrs={'class': 'form-control'}))
    sExam = forms.CharField(widget=forms.Select(choices=sExam_cho, attrs={'class': 'form-control'}))
    sComment = forms.CharField(widget=forms.Select(choices=sComment_cho, attrs={'class': 'form-control'}))
    sQualifaction = forms.CharField(widget=forms.Select(choices=sQuali_cho, attrs={'class': 'form-control'}))
    sFee = forms.IntegerField(widget=forms.Select(choices=sFee_cho, attrs={'class': 'form-control'}))
    sDob = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    sName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sFather = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sPhone1 = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
    sPhone2 = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #sDoa = forms.DateField(widget=forms.TextInput(date.today()))

    class Meta:
        model=StuReg
        fields='__all__'