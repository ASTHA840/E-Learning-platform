from django.urls import path
from . import views

urlpatterns =[
    path("dashboard/",views.dashboard),
    path("category/",views.mycategory),
    path("lectures/",views.lectures),
    path("lecturecat/",views.lecturecat),
    path("enotes/",views.enotes),
    path("softwarekit/",views.software),
    path("signout/",views.signout),
    path("profile/",views.profile),
    path("task/",views.task),
    path("tsubmitted/",views.tsubmitted),
   
]