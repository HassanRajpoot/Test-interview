from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Document, Tag

class DocumentAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.tag = Tag.objects.create(name='test-tag')
        self.document = Document.objects.create(
            title='Test Document',
            content='# Test Content',
            user=self.user
        )
        self.document.tags.add(self.tag)

    def test_create_document(self):
        data = {
            'title': 'New Document',
            'content': '# New Content',
            'tags': [{'name': 'new-tag'}]
        }
        response = self.client.post('/api/documents/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 2)
        self.assertEqual(Tag.objects.count(), 2)

    def test_get_documents(self):
        response = self.client.get('/api/documents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_document(self):
        data = {'title': 'Updated Title'}
        response = self.client.patch(f'/api/documents/{self.document.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_document(self):
        response = self.client.delete(f'/api/documents/{self.document.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Document.objects.count(), 0)
