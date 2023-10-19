from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import User


class Service(models.Model):
    name = models.CharField("Название", max_length=50)
    full_price = models.PositiveIntegerField("Полная цена")

    class Meta:
        ordering = ('name',)
        verbose_name = ('Сервис')
        verbose_name_plural = ('Сервисы')

    def __str__(self):
        return self.name


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Полный'),
        ('student', 'Студентческий'),
        ('discount', 'Корпоративный')
    )
    plan_types = models.CharField("Тарифный план", choices=PLAN_TYPES, max_length=8)
    discount_percent = models.PositiveIntegerField("Скидка", default=0, validators=[MaxValueValidator])

    class Meta:
        ordering = ('discount_percent',)
        verbose_name = ('План')
        verbose_name_plural = ('Планы')

    def __str__(self):
        return self.plan_types


class Subscription(models.Model):
    client = models.ForeignKey(User, related_name='subscriptions', on_delete=models.PROTECT,
                               verbose_name="Пользователь")
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT, verbose_name="Сервис")
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT, verbose_name='План')

    class Meta:
        # ordering = ('client',)
        verbose_name = ('Подписка')
        verbose_name_plural = ('Подписки')

    def __str__(self):
        return f'{self.client} - {self.service}'
