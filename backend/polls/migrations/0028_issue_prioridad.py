# Generated by Django 4.1.7 on 2023-04-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_issue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='prioridad',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
