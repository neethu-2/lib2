from  django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from libraryapp .models import chtable,returnbooktb,fbtb,issuebtb,Finetb,regtable
from . models import bookstb
from django.contrib.auth.models import User
from  datetime import datetime,date 
from django.utils.timezone import utc

class ViewChoiceForm(forms.ModelForm):
    class Meta():
        model=chtable
        fields=('Studentname','Booktitle','Author','Date')

class VIEWBOOKRETURNFORM(forms.ModelForm):
    class Meta():
        model=returnbooktb
        fields=('Regno','Booktitle','Author','Returnstatus','Duedate','Returndate')
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter Email')
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class BooksForm(forms.Form):
    Title=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Bookstock=forms.IntegerField(label='stock ',required=False)
   
    Author=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Publications=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Price=forms.IntegerField(label='rate ',required=False)
    Edition=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    Dateofpublications=forms.DateField(label='Dateofpublications(dd/mm/yyyy)', widget=forms.DateInput(format = '%d/%m/%y'))
    Photo=forms.ImageField()

class UPDATEFORM(forms.ModelForm):
  class Meta():
      model=bookstb
      fields=('Title','Bookstock','Author','Publications','Price','Edition','Dateofpublications','Photo')

class UserFeedbackForm(forms.ModelForm):
  class Meta():
      model=fbtb
      fields=('Name','Email','Feedback')

class UserDonationForm(forms.ModelForm):
  class Meta():
      model=issuebtb
      fields=('Name','Regno','Booktitle','Edition','Author','Publications','Date','Mobile')

class UserPaymentForm(forms.ModelForm):
    class Meta():
        model=Finetb
        fields=('Name','Branch','Amount','Date')

class UserprofileForm(forms.Form):
    class Meta():
        model=regtable
        fields=('Name','Gender','Address','Mobile','Email','Branch','Semester','Regno','Place','Username','Photo')

class usereditform(forms.ModelForm):
    class Meta():
        model=regtable
        fields=('Name','Gender','Address','Mobile','Email','Branch','Semester','Regno','Place')
