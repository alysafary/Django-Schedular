# Generated by Django 5.0.2 on 2024-03-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_task_sent_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
