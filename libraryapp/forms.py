from django import forms
from . models import regtable,chtable,returnbooktb,fbtb,issuebtb,Finetb
from cadmin .models import bookstb
from  datetime import datetime,date 
from django.utils.timezone import utc
class USERREGISTRATIONFORM(forms.Form):
	Name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	choice=[('Male','male'),('Female','female')]
	Gender=forms.ChoiceField(choices=choice,widget=forms.RadioSelect)
	Address=forms.CharField(widget= forms.Textarea(attrs={'class': 'form-control','rows':'5'}),required=True)
	# Mobile = forms.CharField(max_length = 100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Mobile=forms.RegexField(regex=r'^\+?1?\d{10,10}$')
	Email = forms.EmailField(max_length = 100,required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
	
	ed = [
    ("Ec", "ec"),
    ("Eee", "eee"),
    ("Cs", "cs"),
    ("Civil",'civil'),
    ("Mech","mech")
    ]
	Branch = forms.MultipleChoiceField(choices=ed,widget=forms.CheckboxSelectMultiple(attrs={'class':'qual'}))
	sem=[
	('S1','s1'),
	('S2','s2'),
	('S3','s3'),
	('S4','s4'),
	('S5','s5'),
	('S6','s6'),
	('S7','s7'),
	('S8','s8')
	]
	Semester=forms.ChoiceField(choices=sem,widget=forms.RadioSelect)
	Regno=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Place=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Username = forms.CharField(max_length = 100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Password = forms.CharField(max_length = 100,required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	Photo= forms.ImageField()


class LOGINFORM(forms.Form):
	Username = forms.CharField(max_length = 100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Password = forms.CharField(max_length = 100,required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PASSWORDCHANGEFORM(forms.Form):
	
	Oldpassword= forms.CharField(max_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	Newpassword= forms.CharField(max_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	Confirmpassword=forms.CharField(max_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserUpdateForm(forms.ModelForm):
	class Meta():
		model=regtable
		fields=('Name','Gender','Address','Mobile','Email','Branch','Semester','Regno','Place','Username','Photo')
YEARS = [x for x in range(1980, 2022)]
class CHOICEFORM(forms.Form):
	Studentname=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Booktitle=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	Author=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# Date=forms.DateField(label='date(dd/mm/yyyy)', widget=forms.DateInput(format = '%d/%m/%y'))
	Date=forms.DateField(initial="1990-06-21",widget=forms.SelectDateWidget(years=YEARS))
class BOOKRETURNFORM(forms.Form):
	# Studentname=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Regno=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Booktitle=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	Author=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	choice=[('Returnbook','returnbook'),('Renewbook','Renewbook')]
	Returnstatus=forms.ChoiceField(choices=choice,widget=forms.RadioSelect)
	# Duedate=forms.DateField(label='Duedate(dd/mm/yyyy)', widget=forms.DateInput(format = '%d/%m/%y'))

	# Returndate=forms.DateField(label='Returndate(dd/mm/yyyy)', widget=forms.DateInput(format = '%d/%m/%y'))
	Duedate=forms.DateField(initial="1990-06-21",widget=forms.SelectDateWidget(years=YEARS))
	Returndate=forms.DateField(initial="1990-06-21",widget=forms.SelectDateWidget(years=YEARS))
class FbForm(forms.ModelForm):
	class Meta():
		model=fbtb
		fields=('Name','Email','Feedback')

# class ISSUEBOOKFORM(forms.ModelForm):
# 	class Meta():
# 		model=issuebtb
# 		fields=('Name','Regno','Booktitle','Edition','Author','Publications','Date','Mobile','Photo')

class ISSUEBOOKFORM(forms.Form):
	# Studentname=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Regno=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Booktitle=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Edition=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Author=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Publications=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Date=forms.DateField(label='date(dd/mm/yyyy)', widget=forms.DateInput(format = '%d/%m/%y'))
	Mobile=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Photo= forms.ImageField()
	
class ViewBooksForm(forms.ModelForm):
	class Meta():
		model=bookstb
		fields=('Photo',)

class ViewBooksDetailsForm(forms.ModelForm):
	class Meta():
		model=bookstb
		fields=('Title','Bookstock','Author','Publications','Price','Edition','Dateofpublications')

class FineForm(forms.Form):
	# Studentname=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Branch=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Amount=forms.IntegerField(label='fine/ ',required=False)
	# Date=forms.DateField(label='date(dd/mm/yyyy)', widget=forms.DateInput(format = '%d/%m/%y'))
	Date=forms.DateField(initial="1990-06-21",widget=forms.SelectDateWidget(years=YEARS))