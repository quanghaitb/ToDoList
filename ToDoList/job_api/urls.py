
from django.contrib import admin
from django.urls import path, include
from .views import JobDetail, JobList
# from .views import 

app_name = 'job_api'

urlpatterns = [ 
    path('<int:pk>/', JobDetail.as_view(), name = 'detailCreate' ),
    path('', JobList.as_view(), name = 'listCreate' ),
]
