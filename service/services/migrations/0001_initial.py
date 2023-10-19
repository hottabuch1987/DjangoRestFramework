# Generated by Django 3.2.16 on 2023-10-17 20:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_types', models.CharField(choices=[('full', 'Полный'), ('student', 'Студентческий'), ('discount', 'Корпоративный')], max_length=15)),
                ('discount_percent', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator], verbose_name='Скидка')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('full_price', models.PositiveIntegerField(verbose_name='Полная цена')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='services.plan', verbose_name='План')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='services.service', verbose_name='Сервис')),
            ],
        ),
    ]
