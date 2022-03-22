from django.conf.urls import url
from form import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('',views.feedback,name="index"),
    path('submit_feedback',views.submit_feedback,name="submit_feedback"),
    path('about',views.about,name="about"),
    path('feedback',views.feedback,name="feedback")
    


]