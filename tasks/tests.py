from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


# Create your tests here.

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'title': 'Test Task',
            'description': 'Testing my code',
            'status': 'pending',
            'due_date': '2025-12-10T12:00:00Z'
        }

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')



