from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('blog_detail/', views.blog_detail , name='blog_detail'),
    path('blog_list/', views.blog_list , name='blog_list'),
    path('add_blogs/', views.add_blogs , name='add_blogs'),
    path('comments/', views.comments , name='comments'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot_password/', views.forgot_pas , name='forgot_pas'),
    path('verify_otp/', views.verify_otp , name='verify_otp'),
    path('reset_password/', views.reset_pas , name='reset_pas'),
    path('logout/', views.logout_view, name='logout'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)