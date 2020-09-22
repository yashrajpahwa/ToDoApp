# Generated by Django 3.1.1 on 2020-09-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255, null=True)),
                ('deadline', models.DateField(null=True)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('importance', models.CharField(blank=True, choices=[('Very Low', 'Very Low'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Very High', 'Very High')], max_length=255, null=True)),
            ],
        ),
    ]