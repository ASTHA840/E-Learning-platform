from django.urls import path
from . import views

urlpatterns=[

    path("",views.index),
    path("index/",views.index),
    path("aboutus/",views.about),
    path("team/",views.team),
    path("gallery/",views.gallery),
    path("services/",views.services),
    path("contactus/",views.contactus),
    path("login/",views.login),
    path("register/",views.register),
    path("profile/",views.profile),

]