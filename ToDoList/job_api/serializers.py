from rest_framework import serializers
from job.models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title', 'author', 'desciption', 'status', 'deadline', 'level', 'degree_of_urgency', 'type')