from django.urls import path
# from cadmin import views
from libraryapp import views
from django.contrib.auth.views import LoginView
app_name='libraryapp'

urlpatterns = [
	
	path('', views.index, name='index'),
	path('login/', LoginView.as_view(), name='login_url'),
	path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('changepassword/<int:id>/', views.changepassword, name='changepassword'),
    path('home/<int:id>/', views.home, name='home'),
    path('Edit/<int:id>/', views.Edit, name='Edit'),
    path('choice/', views.choice, name='choice'),
    path('returnbook/', views.returnbook, name='returnbook'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('logout/', views.logout, name='logout'),
    path('renew/',views.renew,name='renew'),
    path('feedback/', views.feedback, name='feedback'),
    path('issuebook/', views.issuebook, name='issuebook'),
    path('preview/', views.preview, name='preview'),
    path('viewbooks/', views.viewbooks, name='viewbooks'),
    path('viewbooksdetails/<int:pk>/', views.viewbooksdetails, name='viewbooksdetails'),
    path('bill/', views.bill, name='bill'),
    path('extradays/', views.extradays,name='extradays'),
   
    ]