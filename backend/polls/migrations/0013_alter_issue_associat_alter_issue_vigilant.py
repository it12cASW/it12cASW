# Generated by Django 4.1.7 on 2023-04-05 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0012_alter_issue_associat_alter_issue_creador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='associat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues_associado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='vigilant',
            field=models.ManyToManyField(default='', null=True, related_name='issues_vigiladas', to=settings.AUTH_USER_MODEL),
        ),
    ]
