# Generated by Django 3.2.16 on 2023-10-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_plan_plan_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_types',
            field=models.CharField(choices=[('full', 'Полный'), ('student', 'Студентческий'), ('discount', 'Корпоративный')], max_length=8),
        ),
    ]
