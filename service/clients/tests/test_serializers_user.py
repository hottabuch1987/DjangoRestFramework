from django.test import TestCase
from clients.models import User
from clients.serializers import ClientsSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create(phone_number='89006007060', name='ignat')
        self.user_2 = User.objects.create(phone_number='89006005040', name='oleg')

    def test_ok(self):
        data = ClientsSerializer([self.user_1, self.user_2], many=True).data
        expected_data = [
            {
                'id': self.user_1.id,
                'name': 'ignat',
                'phone_number': '89006007060',
            },
            {
                'id': self.user_2.id,
                'name': 'oleg',
                'phone_number': '89006005040',
            },
        ]
        self.assertEqual(expected_data, data)
