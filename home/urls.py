from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("index.html", views.index, name = "home"),
    path("", views.index, name = "home"),
    path("career", views.career, name = "career"),
    path("career.html", views.career, name = "career"),
    path("inner_page.html", views.inner_page, name = "inner-page"),

]
