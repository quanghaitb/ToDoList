from django.shortcuts import render
from rest_framework import generics
from job.models import Job
from .serializers import JobSerializer
from rest_framework.permissions import SAFE_METHODS,AllowAny, BasePermission,IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions , IsAuthenticated

# Create your views here.
class JobUserWritePermission(BasePermission):
    message = 'Editting jobs is restricted to the author only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
    

class JobList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.jobobject.all()
    serializer_class = JobSerializer

class JobFilter(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def has_author(self):
        user = self.request.user
        return Job.objects.filter(author = user)

class JobDetail(generics.RetrieveUpdateAPIView, JobUserWritePermission):
    permission_classes = [JobUserWritePermission]
    queryset = Job.objects.all()
    serializer_class = JobSerializer