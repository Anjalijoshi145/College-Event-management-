"""
URL configuration for Web_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path,include
from Home_App import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name='Home'),
    path('home',views.home,name='Home'),
    path("dashboard",views.dashboard,name='Dashboard'),


    path("about", views.about,name='About Us'),
    path("event", views.event,name='Events'),
    path("contact",views.contact,name='Contact Us'),
    path("loginpage",views.loginpage,name='Login'),


    path("logout",views.logoutUser,name='Logout'),
    path("register",views.register,name='Register'),
    path("eventregister",views.eventregister,name='REGISTER'),
    path("create_event",views.createEvents,name='Events'),


    path("update_event/<str:pk>/",views.updateEvent,name='update_event'),
    path("delete_event/<str:pk>/",views.deleteEvent,name='delete_event'),
    path("userprofile",views.UserProfile,name='userprofile'),
    path("student/<int:student_id>/",views.student,name='student'),


    path("settings",views.account_settings,name='Settings'),
    path("reset_password",auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path("reset_password_send",auth_views.PasswordResetDoneView.as_view(template_name='password_reset_send.html'),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path("reset_password_complete",auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


    path("contact_us",views.contact_us,name='Contact_Us'),
    path("register_events",views.register_events,name='Registered_Events'),
    path("student_info",views.Students_info,name='Students'),

    path("delete_student/<int:student_id>/",views.deletestudent,name='delete_student'),
    path("delete_contact/<int:contact_id>/",views.deletecontact,name='delete_contact'),
    path("delete_register_event/<int:event_id>/",views.deleteregisterevent,name='delete_register_event'),
   


   
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        
    
