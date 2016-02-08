from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Article
from super.settings.base import DEFAULT_USER, DEFAULT_PASS


class SecurityTests(APITestCase):

    def test_negative(self):
        """
        Ensure access is denied.
        """
        url = reverse('api:article-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_positive(self):
        """
        Ensure access is granted.
        """
        url = reverse('api:article-list')
        self.client.login(username=DEFAULT_USER, password=DEFAULT_PASS)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        """
        Verifies JSON response.
        """
        url = reverse('api:article-list')
        self.client.login(username=DEFAULT_USER, password=DEFAULT_PASS)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.count(), len(response.data['articles']))

        expected = ['success', 'articles', 'total_elements']
        self.assertEqual(len(set(response.data.keys()).intersection(expected)), len(expected))