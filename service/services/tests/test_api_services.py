from rest_framework import status
from services.models import Service
from rest_framework.test import APITestCase
from django.urls import reverse
from clients.models import User
from services.models import Subscription, Service, Plan
from services.serializers import SubscriptionSerializer, PlanSerializer, ServiceSerializer


class PlanApiTest(APITestCase):
    def setUp(self):
        self.plan_1 = Plan.objects.create(plan_types='Полный', discount_percent='0')
        self.plan_2 = Plan.objects.create(plan_types='Студен', discount_percent='10')
        self.plan_3 = Plan.objects.create(plan_types='Твой', discount_percent='20')

    def test_get(self):
        url = reverse('plan-list')
        response = self.client.get(url)
        serializer_data = PlanSerializer([self.plan_1, self.plan_2, self.plan_3], many=True).data
        # print(response.data)
        # print(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # print(response.status_code)
        self.assertEqual(serializer_data, response.data)


class ServiceApiTest(APITestCase):
    def setUp(self):
        self.service_1 = Service.objects.create(name='Обслуживание', full_price='2500')
        self.service_2 = Service.objects.create(name='Ремонт', full_price='1800')

    def test_get(self):
        url = reverse('service-list')
        response = self.client.get(url)
        serializer_data = ServiceSerializer([self.service_1, self.service_2], many=True).data
        # print(response.data)
        # print(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # print(response.status_code)
        self.assertEqual(serializer_data, response.data)


class SubscriptionApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name='Test_Katia', phone_number='890900908')
        self.service = Service.objects.create(name='Ремонт', full_price='3500')
        self.plan = Plan.objects.create(plan_types='full', discount_percent=10)
        self.subscription_1 = Subscription.objects.create(client=self.user, service=self.service, plan=self.plan)
        self.subscription_2 = Subscription.objects.create(client=self.user, service=self.service, plan=self.plan)

    def test_get(self):
        url = reverse('subscriptions-list')
        response = self.client.get(url)
        serializer_data = SubscriptionSerializer([self.subscription_1, self.subscription_2], many=True).data
        print(response.data)
        print(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

