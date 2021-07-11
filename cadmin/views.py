from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from. forms import BooksForm
from .forms import VIEWBOOKRETURNFORM,ViewChoiceForm,UPDATEFORM,UserFeedbackForm,UserDonationForm,UserPaymentForm,UserprofileForm,usereditform
from. models import bookstb
from libraryapp.models import chtable,returnbooktb,fbtb,issuebtb,Finetb,regtable
from libraryapp.forms import CHOICEFORM,BOOKRETURNFORM,FbForm,ISSUEBOOKFORM,FineForm,USERREGISTRATIONFORM

def index1(request):
    return render(request,'cadmin/index.html')


def AdminRegister(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('Success')
            

            # messages.success(request, 'Account created successfully')
            # return redirect('login_url')

    else:
        f = CustomUserCreationForm()

    return render(request,'cadmin/AdminRegister.html', {'form':f})
@login_required
def dashboardView(request):
    return render(request,'cadmin/index.html')
@login_required   
def indexView(request):
    return render(request,'registration/indexView.html')
def Home(request,id):
    if request.session.has_key:
        uid=request.session["id"]
        user=auth_user.objects.get(id=id)
        return render(request,'cadmin/index.html',{'user':user})


def books(request):
    saved=False
    if request.method=='POST':
        MyProfileForm=BooksForm(request.POST  or None, request.FILES or None)
        if MyProfileForm.is_valid():
            bbtb=bookstb()
            bbtb.Title=MyProfileForm.cleaned_data['Title']
            bbtb.Bookstock=MyProfileForm.cleaned_data['Bookstock']
            bbtb.Author=MyProfileForm.cleaned_data['Author']
            bbtb.Publications=MyProfileForm.cleaned_data['Publications']
            bbtb.Price=MyProfileForm.cleaned_data['Price']
            bbtb.Edition=MyProfileForm.cleaned_data['Edition']
            bbtb.Dateofpublications=MyProfileForm.cleaned_data['Dateofpublications']
            bbtb.Photo=MyProfileForm.cleaned_data['Photo']
            
            bbtb.save()
            return HttpResponse('Success')
            

        else:
            print(MyProfileForm.errors)
            return render(request, 'cadmin/books.html',{'data':MyProfileForm})
        
    else:       
        MyProfileForm=BooksForm()
        return render(request, 'cadmin/books.html',{'data':MyProfileForm})

def userchoice(request):
    fm=ViewChoiceForm()
    stud=chtable.objects.all()
    return render(request,'cadmin/userchoice.html',{'form':fm,'stu':stud})

def viewreturnbook(request):
    fm=VIEWBOOKRETURNFORM()
    stud=returnbooktb.objects.all()
    return render(request,'cadmin/viewreturnbook.html',{'form':fm,'stu':stud})

def update(request):
  fm=UPDATEFORM()
  stud=bookstb.objects.all()
  return render(request,'cadmin/update.html',{'form':fm,'stu':stud})

def EditBook(request,id):
  user=bookstb.objects.get(id=id)
  data=UPDATEFORM(request.POST or None,request.FILES or None,instance=user)
  if data.is_valid():
      data.save()
        
  return render(request,'cadmin/EditBook.html',{'data':data, 'user':user})

def delete_data(request,id):
    if request.method == 'POST':
        pi=get_object_or_404(bookstb,id=id)
        pi.delete()
        return HttpResponse('Success')
def delete_data1(request,id):
    if request.method == 'POST':
        pi=get_object_or_404(chtable,id=id)
        pi.delete()
        return HttpResponse('Success')
def delete_data2(request,id):
    if request.method == 'POST':
        pi=get_object_or_404(returnbooktb,id=id)
        pi.delete()
        return HttpResponse('Success')
    
def Logout(request):
    messages.info(request,'loggedout successfully')
    return redirect('/')
    
def userfeedback(request):
    fm=UserFeedbackForm()
    stud=fbtb.objects.all()
    return render(request,'cadmin/userfeedback.html',{'form':fm,'stu':stud})

def donation(request):
    fm=UserDonationForm()
    stud=issuebtb.objects.all()
    return render(request,'cadmin/donation.html',{'form':fm,'stu':stud})
def userpaymentdetails(request):
    fm=UserPaymentForm()
    stud=Finetb.objects.all()
    return render(request,'cadmin/userpaymentdetails.html',{'form':fm,'stu':stud})
def userprofile(request):
    fm=UserprofileForm()
    stud=regtable.objects.all()
    return render(request,'cadmin/userprofile.html',{'form':fm,'stu':stud})
def Edituserprofile(request,id):
  user=regtable.objects.get(id=id)
  data=usereditform(request.POST or None,request.FILES or None,instance=user)
  if data.is_valid():
      data.save()
        
  return render(request,'cadmin/Edituserprofile.html',{'data':data, 'user':user})
