# Generated by Django 4.1.7 on 2023-04-05 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0011_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='associat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='issues_associado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues_creadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='vigilant',
            field=models.ManyToManyField(default='', related_name='issues_vigiladas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
