from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf.urls import url, include
# from libraryapp import views
from cadmin import views
app_name='cadmin'

urlpatterns = [
    
    path('', views.index1, name='index1'),
    url(r'^AdminRegister/$', views.AdminRegister, name='AdminRegister'),

    path('login/',LoginView.as_view(),name='login_url'), 
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('indexView',views.indexView,name='indexView'), 
    path('books/', views.books, name='books'),
    path('userchoice/', views.userchoice, name='userchoice'),
    path('viewreturnbook/', views.viewreturnbook, name='viewreturnbook'),
    path('delete_data/<int:id>/', views.delete_data, name='delete_data'),
    path('delete_data1/<int:id>/', views.delete_data1, name='delete_data1'),
    path('delete_data2/<int:id>/', views.delete_data2, name='delete_data2'),
    path('EditBook/<int:id>/', views.EditBook, name='EditBook'),
    path('update/', views.update, name='update'),
    path('Logout/', views.Logout, name='Logout'),
    path('userfeedback/', views.userfeedback, name='userfeedback'),
    path('donation/', views.donation, name='donation'),
    path('userpaymentdetails/', views.userpaymentdetails,name='userpaymentdetails'),
    path('userprofile/', views.userprofile,name='userprofile'),
    path('Edituserprofile/<int:id>/', views.Edituserprofile, name='Edituserprofile')
    ]