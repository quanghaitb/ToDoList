
from django.contrib import admin
from django.urls import path, include
from .views import JobList
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'job_api'

routes = DefaultRouter()

routes.register('', JobList, basename= 'job')   
urlpatterns = routes.urls


# urlpatterns = [ 
#     path('<int:pk>/', PostList.as_view(), name = 'detailCreate' ),
#     path('', PostList.as_view(), name = 'listCreate' ),
# ]
