# Generated by Django 5.0.4 on 2024-04-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_employee_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
