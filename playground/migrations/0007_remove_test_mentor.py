# Generated by Django 4.2 on 2023-11-25 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='mentor',
        ),
    ]