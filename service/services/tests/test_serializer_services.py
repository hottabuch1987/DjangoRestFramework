from django.test import TestCase
from services.models import Plan, Service, Subscription
from services.serializers import ServiceSerializer, PlanSerializer, SubscriptionSerializer


class PlanSerializerTestCase(TestCase):
    def setUp(self):
        self.plan_1 = Plan.objects.create(plan_types='Полный', discount_percent='0')
        self.plan_2 = Plan.objects.create(plan_types='Студент', discount_percent='10')
        self.plan_3 = Plan.objects.create(plan_types='Персон', discount_percent='15')

    def test_ok(self):
        data = PlanSerializer([self.plan_1, self.plan_2, self.plan_3], many=True).data
        expected_data = [
            {
                'id': self.plan_1.id,
                'plan_types': 'Полный',
                'discount_percent': 0,
            },
            {
                'id': self.plan_2.id,
                'plan_types': 'Студент',
                'discount_percent': 10,
            },
            {
                'id': self.plan_3.id,
                'plan_types': 'Персон',
                'discount_percent': 15,
            },
        ]
        self.assertEqual(expected_data, data)


class ServiceSerializerTestCase(TestCase):
    def setUp(self):
        self.service_1 = Service.objects.create(name='Ремонт', full_price='2400')
        self.service_2 = Service.objects.create(name='Обслуж', full_price='3500')

    def test_ok(self):
        data = ServiceSerializer([self.service_1, self.service_2], many=True).data
        expected_data = [
            {
                'id': self.service_1.id,
                'name': 'Ремонт',
                'full_price': 2400.00,
            },
            {
                'id': self.service_2.id,
                'name': 'Обслуж',
                'full_price': 3500.00,
            },
        ]
        self.assertEqual(expected_data, data)
