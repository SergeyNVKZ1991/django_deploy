from unittest import TestCase

from rest_framework.test import APIClient


class TestSomething(TestCase):
    def test_sample_view(self):
        client = APIClient()
        URL = '/current_time/'
        response = client.get(URL)
        assert response.status_code == 200
