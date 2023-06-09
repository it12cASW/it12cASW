# Generated by Django 4.1.7 on 2023-04-13 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_alter_issue_blocked_alter_issue_prioridad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad_issue',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='polls.issue'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
