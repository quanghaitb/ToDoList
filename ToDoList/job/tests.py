from django.test import TestCase
from django.contrib.auth.models import User
from job.models import Job, Type
# Create your tests here.

class Test_Create_Job(TestCase):
    @classmethod
    def setUpTestData(cls):
        testType = Type.objects.create(name='cong viec')
        test_user = User.objects.create_user(username='test_user', password = '123456789')
        test_job = Job.objects.create(type_id = 1, title='test title', desciption = 'test description', author_id = 1, status = 'finished', level = 'urgent', degree_of_urgency = 'important')
    def test_Job_content(self):
        job = Job.jobobject.get(id = 1)
        typ = Type.objects.get(id =  1)
        description  = f'{job.desciption}'
        author  = f'{job.author}'
        title  = f'{job.title}'
        status  = f'{job.status}'
        level =  f'{job.level}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'job title')
        self.assertEqual(description, 'job description')
        self.assertEqual(level, 'job level')
        self.assertEqual(status, 'published')
        self.assertEqual(str(job), 'job title')
        self.assertEqual(str(typ), 'cong viec')
