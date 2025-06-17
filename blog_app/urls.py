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
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)