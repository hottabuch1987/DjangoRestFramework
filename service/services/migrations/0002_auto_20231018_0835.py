# Generated by Django 3.2.16 on 2023-10-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ('discount_percent',), 'verbose_name': 'План', 'verbose_name_plural': 'Планы'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('name',), 'verbose_name': 'Сервис', 'verbose_name_plural': 'Сервисы'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('client',), 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_types',
            field=models.CharField(choices=[('Полный', 'full'), ('Студентческий', 'student'), ('Корпоративный', 'discount')], max_length=15),
        ),
    ]
