# Generated by Django 5.0.4 on 2024-05-03 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0011_alter_test_time_limit_per_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
