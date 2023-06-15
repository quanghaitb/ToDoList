from django.shortcuts import render
from rest_framework import generics
from job.models import Job
from .serializers import JobSerializer
from  rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.permissions import SAFE_METHODS,AllowAny, BasePermission,IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions , IsAuthenticated

# Create your views here.
class JobUserWritePermission(BasePermission):
    message = 'Editting jobs is restricted to the author only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
    
    
    
class JobList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = JobSerializer
    def get_object(self, queryset= None, **kwargs):
        item  = self.kwargs.get('pk')
        return get_object_or_404(Job, title=item)
    def get_queryset(self):
        return Job.objects.all()
    
    
# class JobList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Job.jobobject.all()
    
#     def list(self, request):
#         serializer_class = JobSerializer(self.queryset, many = True)
#         return Response(serializer_class.data)        
    
#     def retrieve(self, request, pk=None):
#         job = get_object_or_404(self.queryset, pk = pk)
#         serializer_class = JobSerializer(job)
#         return Response(serializer_class.data)
        
    
    
    
    
# class JobList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Job.jobobject.all()
#     serializer_class = JobSerializer

# class JobFilter(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     def has_author(self):
#         user = self.request.user
#         return Job.objects.filter(author = user)

# class JobDetail(generics.RetrieveUpdateAPIView, JobUserWritePermission):
#     permission_classes = [JobUserWritePermission]
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer

