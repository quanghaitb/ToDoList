from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Job(models.Model):
    class JobObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='unfinished')
        
    options = (
        ('finished','Finished'),
        ('unfinished', 'Unfinished')
    )
    options_level = (
        ('urgent','Urgent'),
        ('hastiness', 'Hastiness')
    )
    options_degree = (
        ('important','Important'),
        ('not important', 'Not important')
    )
    
    type = models.ForeignKey(Type, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    desciption = models.TextField()
    status = models.CharField(max_length=250, choices=options, default='unfinished')
    level = models.CharField(max_length=250, choices=options_level, default='hastiness')
    degree_of_urgency = models.CharField(max_length=250, choices=options_degree,default='not important')
    deadline = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'todo_job')
    objects = models.Manager()
    jobobject = JobObjects()
    class Meta:
        ordering = ('-deadline',)
    def __str__(self):
        return self.title
    
    