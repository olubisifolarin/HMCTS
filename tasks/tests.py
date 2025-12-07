from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from .models import Task

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {
            'title': 'Test Task',
            'description': 'Just testing',
            'status': 'pending',
            'due_date': (timezone.now() + timezone.timedelta(days=1)).isoformat()
        }

    def test_create_task_success(self):
        response = self.client.post('/api/tasks/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_create_task_missing_title(self):
        bad = self.valid_data.copy()
        bad['title'] = ''
        response = self.client.post('/api/tasks/', bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data['errors'])

    def test_create_task_due_date_in_past(self):
        bad = self.valid_data.copy()
        bad['due_date'] = (timezone.now() - timezone.timedelta(days=1)).isoformat()
        response = self.client.post('/api/tasks/', bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('due_date', response.data['errors'])
