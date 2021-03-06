# Generated by Django 3.1.1 on 2020-09-23 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=255, null=True)),
                ('deadline', models.DateField(null=True)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('importance', models.CharField(blank=True, choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Very High', 'Very High')], max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('completed', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
