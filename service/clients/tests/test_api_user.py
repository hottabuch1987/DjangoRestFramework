from rest_framework.test import APITestCase
from django.urls import reverse
from clients.models import User
from clients.serializers import ClientsSerializer
from rest_framework import status


class UserApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create(phone_number='89006007060', name='ignat')
        self.user_2 = User.objects.create(phone_number='89006005040', name='oleg')

    def test_get(self):
        url = reverse('clients-list')
        response = self.client.get(url)
        #print(response.data)
        serializer_data = ClientsSerializer([self.user_1, self.user_2], many=True).data
        #print(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        #print(response.status_code)
        self.assertEqual(serializer_data, response.data)

