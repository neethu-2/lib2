from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import USERREGISTRATIONFORM,PASSWORDCHANGEFORM,LOGINFORM,UserUpdateForm,CHOICEFORM,BOOKRETURNFORM,FbForm,ISSUEBOOKFORM,FineForm
from .models import regtable,chtable,returnbooktb,fbtb,issuebtb,Finetb
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt
from cadmin.models import bookstb
from cadmin.forms import BooksForm
from . forms import ViewBooksDetailsForm,ViewBooksForm

def index(request):
	return render(request, 'libraryapp/index.html')
	
def preview(request):
	return render(request, 'libraryapp/preview.html')
def extradays(request):
	return render(request, 'libraryapp/extradays.html')
def register(request):
	saved=False
	if request.method=='POST':
		MyProfileForm=USERREGISTRATIONFORM(request.POST or None, request.FILES or None)
		if MyProfileForm.is_valid():
			vlatb=regtable()
			vlatb.Name=MyProfileForm.cleaned_data['Name']
			vlatb.Gender=MyProfileForm.cleaned_data['Gender']
			vlatb.Address=MyProfileForm.cleaned_data['Address']
			vlatb.Mobile=MyProfileForm.cleaned_data['Mobile']
			vlatb.Email=MyProfileForm.cleaned_data['Email']
			qua=MyProfileForm.cleaned_data['Branch']
			vlatb.Branch=',' .join(qua)
			vlatb.Semester=MyProfileForm.cleaned_data['Semester']
			vlatb.Regno=MyProfileForm.cleaned_data['Regno']
			vlatb.Place=MyProfileForm.cleaned_data['Place']
			vlatb.Username=MyProfileForm.cleaned_data['Username']
			vlatb.Password=MyProfileForm.cleaned_data['Password']
			vlatb.Photo=MyProfileForm.cleaned_data['Photo']
		
			vlatb.save()
			return HttpResponse('Success')
		else:
			print(MyProfileForm.errors)
			return render(request, 'libraryapp/register.html',{'data':MyProfileForm})
	else:		
		MyProfileForm=USERREGISTRATIONFORM()
		return render(request, 'libraryapp/register.html',{'data':MyProfileForm})



def user_login(request):
	if request.method=='POST':
		form=LOGINFORM(request.POST)
		if form.is_valid():
			Username=form.cleaned_data["Username"]
			Password=form.cleaned_data["Password"]
			a=regtable.objects.all().filter(Username=Username,Password=Password)
			for x in a:
				request.session['sid']=x.id
				return redirect('/home/%s' % x.id)
			else:
				return HttpResponse('Invalid Credentials')


		else:
			print(form.errors)
			return render(request,'libraryapp/user_login.html',{'data':form})
	else:
		form=LOGINFORM()
		return render(request,'libraryapp/user_login.html',{'data':form})


def changepassword(request,id):
	
    user=regtable.objects.get(id=id)
    if request.method=='POST':
        form=PASSWORDCHANGEFORM(request.POST or None,request.FILES or None)
        if form.is_valid():
            oldpassword = form.cleaned_data['Oldpassword']
            newpassword = form.cleaned_data['Newpassword']
            confirmpassword = form.cleaned_data['Confirmpassword']
            if oldpassword!=user.Password:
                msg="Enter correctpassword"
                return render(request,'libraryapp/changepassword.html',{'form':form,'error':msg,'user':user})
            elif newpassword!=confirmpassword:
                msg="Password does not match"
                return render(request,'libraryapp/changepassword.html',{'form':form,'error':msg,'user':user})
            else:
                user.Password =newpassword
                user.Confirmpassword = confirmpassword
                user.save()
                return HttpResponse('Success')
                # msg ="Password Change Successfully"
                return redirect('/home/%s' % user.id)
                return render(request,'libraryapp/changepassword.html',{'form':form,'error':msg,'user':user})
    else:
        form=PASSWORDCHANGEFORM()
        return render(request,'libraryapp/changepassword.html',{'form':form,'user':user})
       
 
def home(request,id):
	if request.session.has_key:
		uid=request.session['sid']
		user=regtable.objects.get(id=id)
		return render(request,'libraryapp/home.html',{'user':user})

def Edit(request,id):
	user=regtable.objects.get(id=id)
	form=UserUpdateForm(request.POST or None,request.FILES or None,instance=user)
	if form.is_valid():
		form.save()
		return redirect('/home/%s' % user.id)
	return render(request,'libraryapp/Edit.html',{'form':form, 'user':user})
def choice(request):
	saved=False
	if request.method=='POST':
		FileForm=CHOICEFORM(request.POST or None, request.FILES or None)
		if FileForm.is_valid():
			vstb=chtable()
			
			vstb.Studentname=FileForm.cleaned_data['Studentname']
			
			
			vstb.Booktitle=FileForm.cleaned_data['Booktitle']
			
			vstb.Author=FileForm.cleaned_data['Author']
			vstb.Date=FileForm.cleaned_data['Date']
			vstb.save()
			return HttpResponse('Success')

		else:
			print(FileForm.errors)
			return render(request, 'libraryapp/choice.html',{'data':FileForm})
	else:		
		FileForm=CHOICEFORM()
		return render(request, 'libraryapp/choice.html',{'data':FileForm})

def returnbook(request):
	saved=False
	if request.method=='POST':
		File=BOOKRETURNFORM(request.POST)
		if File.is_valid():
			vctb=returnbooktb()
			# rttb.Studentname=File.cleaned_data['Studentname']
			vctb.Regno=File.cleaned_data['Regno']
			vctb.Booktitle=File.cleaned_data['Booktitle']
			
			vctb.Author=File.cleaned_data['Author']
			vctb.Returnstatus=File.cleaned_data['Returnstatus']
			vctb.Duedate=File.cleaned_data['Duedate']
			vctb.Returndate=File.cleaned_data['Returndate']
			vctb.save()
			return HttpResponse('Success')
		else:
			print(File.errors)
			return render(request, 'libraryapp/returnbook.html',{'data':File})
	else:		
		File=BOOKRETURNFORM()
		return render(request, 'libraryapp/returnbook.html',{'data':File})


def delete(request,id):
	user=regtable.objects.get(id=id)
	user.delete()
	return redirect('/')

def logout(request):
	messages.info(request,'loggedout successfully')
	return redirect('/')
def renew(request):
	# return HttpResponse('Success')
	return render(request, 'libraryapp/renew.html')

def feedback(request):
	saved=False
	if request.method=='POST':
		FileForm=FbForm(request.POST or None, request.FILES or None)
		if FileForm.is_valid():
			vdtb=fbtb()

			vdtb.Name=FileForm.cleaned_data['Name']
			vdtb.Email=FileForm.cleaned_data['Email']
			vdtb.Feedback=FileForm.cleaned_data['Feedback']
			
			vdtb.save()
			return HttpResponse('Success')

		else:
			print(FileForm.errors)
			return render(request, 'libraryapp/feedback.html',{'data':FileForm})
	else:		
		FileForm=FbForm()
		return render(request, 'libraryapp/feedback.html',{'data':FileForm})


def issuebook(request):
	saved=False
	if request.method=='POST':
		MyProfileForm=ISSUEBOOKFORM(request.POST  or None, request.FILES or None)
		if MyProfileForm.is_valid():
			istb=issuebtb()
			istb.Name=MyProfileForm.cleaned_data['Name']
			istb.Regno=MyProfileForm.cleaned_data['Regno']
			istb.Booktitle=MyProfileForm.cleaned_data['Booktitle']
			istb.Edition=MyProfileForm.cleaned_data['Edition']
			istb.Author=MyProfileForm.cleaned_data['Author']
			istb.Publications=MyProfileForm.cleaned_data['Publications']
			istb.Date=MyProfileForm.cleaned_data['Date']
			istb.Mobile=MyProfileForm.cleaned_data['Mobile']
			istb.Photo=MyProfileForm.cleaned_data['Photo']
		
			istb.save()
			return HttpResponse('Success')
		else:
			print(MyProfileForm.errors)
			return render(request, 'libraryapp/issuebook.html',{'data':MyProfileForm})
	else:		
		MyProfileForm=ISSUEBOOKFORM()
		return render(request, 'libraryapp/issuebook.html',{'data':MyProfileForm})

def viewbooks(request):
    Img=bookstb.objects.all()
    
    return render(request,'libraryapp/viewbooks.html',{'Img':Img})

def viewbooksdetails(request,pk):
	user=bookstb.objects.get(id=pk)
	data=ViewBooksDetailsForm(request.POST or None,request.FILES or None,instance=user)
	if data.is_valid():
		data.save()
		return redirect('/viewbooks/%s' % user.id)
	return render(request,'libraryapp/viewbooksdetails.html',{'data':data, 'user':user})
def bill(request):
	saved=False
	if request.method=='POST':
		MyProfileForm=FineForm(request.POST  or None, request.FILES or None)
		if MyProfileForm.is_valid():
			fntb=Finetb()
			fntb.Name=MyProfileForm.cleaned_data['Name']
			fntb.Branch=MyProfileForm.cleaned_data['Branch']
			fntb.Amount=MyProfileForm.cleaned_data['Amount']
			fntb.Date=MyProfileForm.cleaned_data['Date']
			
			
			fntb.save()
			return HttpResponse('Payment Successfull')
			

		else:
			print(MyProfileForm.errors)
			return render(request, 'libraryapp/bill.html',{'data':MyProfileForm})
		
	else:		
		MyProfileForm=FineForm()
		return render(request, 'libraryapp/bill.html',{'data':MyProfileForm})


# def viewchoice(request):
# 	fm=UserChoiceForm()
# 	stud=choicetable.objects.all()
# 	return render(request,'libapp/viewchoice.html',{'form':fm,'stu':stud})
