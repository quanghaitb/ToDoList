from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from job.models import Job, Type
from django.contrib.auth.models import User

class JobTests(APITestCase):
    def test_view_post(self):
        url = reverse('job_api:listCreate')
        response = self.client.get(url, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def create_job(self):
        self.test_job = Type.objects.create(name='Ngoai')
        self.test_user1 = User.objects.create_user(username='test_user1', password='123456789')
        data = {'title':'test title', 'desciption' : 'test description', 'status' : 'finished', 'level' : 'urgent', 'degree_of_urgency' : 'important'}

        url = reverse('job_api:listCreate')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)