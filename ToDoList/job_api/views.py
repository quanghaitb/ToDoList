from django.shortcuts import render
from rest_framework import generics
from job.models import Job
from .serializers import JobSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
class JobList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Job.jobobject.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer