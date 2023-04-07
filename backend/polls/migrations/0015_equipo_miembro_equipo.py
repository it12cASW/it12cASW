# Generated by Django 4.1.7 on 2023-04-07 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0014_actividad_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos_creados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Miembro_Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(default='', max_length=50)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.equipo')),
                ('miembro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
