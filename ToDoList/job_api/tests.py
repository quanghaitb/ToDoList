from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from job.models import Job, Type
from django.contrib.auth.models import User
from rest_framework.test import APIClient


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
    def test_job_update(self):
        client = APIClient()
        self.test_type = Type.objects.create(name= 'cong viec')
        self.test_user1 = User.objects.create_user(username='test_user1', password='123456789')
        self.test_user2 = User.objects.create_user(username='test_user2', password='123456789')
        test_data = {'title':'test title', 'desciption' : 'test description', 'status' : 'finished', 'level' : 'urgent', 'degree_of_urgency' : 'important'}
        client.login(username = self.test_user2.username, password = '123456789')
        url = reverse(('job_api:detailCreate'), kwargs={'pk':3})
        response = client.put(
            url, 
                {
                    "title": "Tập thể dục",
                    "author": 1,
                    "desciption": "Tập thể dục buổi sáng",
                    "status": "unfinished",
                    "deadline": "2023-06-30T18:45:00Z",
                    "level": "hastiness",
                    "degree_of_urgency": "not important",
                    "type": 3
                }, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        