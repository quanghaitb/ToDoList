
from django.contrib import admin
from django.urls import path, include
from .views import JobDetail, JobList, JobFilter
# from .views import 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'job_api'

urlpatterns = [ 
    path('<int:pk>/', JobDetail.as_view(), name = 'detailCreate' ),
    path('', JobList.as_view(), name = 'listCreate' ),
]
