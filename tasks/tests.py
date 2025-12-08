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

  
    # CREATE TASK TESTS
   
    def test_create_task_success(self):
        """Test creating a task with valid data"""
        response = self.client.post('/api/tasks/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, self.valid_data['title'])

    def test_create_task_missing_title(self):
        """Test creating a task with missing title"""
        bad = self.valid_data.copy()
        bad['title'] = ''
        response = self.client.post('/api/tasks/', bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data['errors'])

    def test_create_task_due_date_in_past(self):
        """Test creating a task with a due date in the past"""
        bad = self.valid_data.copy()
        bad['due_date'] = (timezone.now() - timezone.timedelta(days=1)).isoformat()
        response = self.client.post('/api/tasks/', bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('due_date', response.data['errors'])

    def test_create_task_invalid_status(self):
        """Test creating a task with an invalid status value"""
        bad = self.valid_data.copy()
        bad['status'] = 'invalid_status'
        response = self.client.post('/api/tasks/', bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('status', response.data['errors'])

    def test_create_task_empty_description(self):
        """Test creating a task with an empty description"""
        bad = self.valid_data.copy()
        bad['description'] = ''
        response = self.client.post('/api/tasks/', bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('description', response.data['errors'])


    def test_list_tasks_empty(self):
        """Test GET /api/tasks/ returns empty list when no tasks exist"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_list_tasks_non_empty(self):
        """Test GET /api/tasks/ returns tasks correctly"""
        Task.objects.create(**self.valid_data)
        Task.objects.create(
            title='Another Task',
            description='Second task',
            status='pending',
            due_date=(timezone.now() + timezone.timedelta(days=2))
        )
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        titles = [task['title'] for task in response.data]
        self.assertIn('Test Task', titles)
        self.assertIn('Another Task', titles)
